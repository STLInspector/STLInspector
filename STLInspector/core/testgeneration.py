from z3 import z3
import multiprocessing
from multiprocessing.pool import ThreadPool
import random
from temporallogic import *


class Mutant:
    """
    Represents a mutant.

    Attributes:
        formula (Clause) : Temporal logic formula that represents the mutant.
        z3string_pos (str) : String representing the formula in z3 syntax that can be parsed by z3.parse_smt2_string.
        z3string_neg (str) : String representing the negated formula in z3 syntax.
        cons_strings (list) : List of strings in z3 syntax representing the constants used in the mutant's formula.
        killed (bool) : Boolean indicating whether the mutant has been killed.
    """

    def __init__(self, dictionary=None, formula=None, z3string_pos=None, z3string_neg=None, cons_strings=None):
        if dictionary is not None:
            self.deserialize(dictionary)
        else:
            self.formula = formula
            self.formula_text = formula.__str__()
            self.z3string_pos = z3string_pos
            self.z3string_neg = z3string_neg
            self.cons_strings = cons_strings
            self.z3_pos = None  # positive z3 instance is computed and set later in method initialize
            self.z3_neg = None  # negative z3 instance is computed and set later in method initialize
            self.killed = False

    def serialize(self):
        dictionary = dict()
        dictionary['formula_text'] = self.formula_text
        dictionary['z3string_pos'] = self.z3string_pos
        dictionary['z3string_neg'] = self.z3string_neg
        dictionary['constants'] = self.cons_strings
        dictionary['killed'] = self.killed
        return dictionary

    def deserialize(self, dictionary):
        self.formula_text = dictionary['formula_text']
        self.z3string_pos = dictionary['z3string_pos']
        self.z3string_neg = dictionary['z3string_neg']
        self.cons_strings = dictionary['constants']
        self.z3_pos = z3.parse_smt2_string(self.z3string_pos)
        self.z3_neg = z3.parse_smt2_string(self.z3string_neg)
        self.killed = dictionary['killed']


def generate_mutants(formula, tio_lower_bound=None, tio_upper_bound=None):
    mutants = dict()

    mutants['rro'] = [x for x in formula.rro() if not x == formula]
    mutants['tio'] = [x for x in formula.tio(tio_lower_bound, tio_upper_bound) if not x == formula]
    mutants['io'] = [x for x in formula.io() if not x == formula]
    mutants['mto'] = [x for x in formula.mto() if not x == formula]
    mutants['ano'] = [x for x in formula.ano() if not x == formula]
    mutants['eno'] = [x for x in formula.eno() if not x == formula]
    mutants['oro'] = [x for x in formula.oro(formula.get_aps()) if not x == formula]
    mutants['lro'] = [x for x in formula.lro() if not x == formula]
    mutants['tro'] = [x for x in formula.tro() if not x == formula]
    mutants['sto0'] = [x for x in formula.sto(0) if not x == formula]
    mutants['sto1'] = [x for x in formula.sto(1) if not x == formula]
    mutants['mco'] = [x for x in formula.mco() if not x == formula]
    mutants['aso'] = [x for x in formula.aso() if not x == formula]

    return mutants


def does_test_kill(original_pos, original_neg, formula_pos, formula_neg, test, cons):
    """
    Checks whether the given test kills the given formula.

    Args:
        original_pos (z3 instance) : Positive encoded temporal logic formula for which test was generated.
        original_neg (z3 instance) : Negative encoded temporal logic formula for which test was generated.
        formula_pos (z3 instance) : Positive encoded temporal logic formula that is checked against the given test.
        formula_neg (z3 instance) : Negative encoded temporal logic formula that is checked against the given test.
        test (z3 model) : Test signal that either does or does not kill the given formula.
        cons (list) : z3 instances of constants used in test and formula.

    Returns:
        bool : True if test kills the given formula, else false.
    """
    s = z3.Solver()
    s.add(z3.Or(z3.And(original_pos, z3.And(stl_model_to_cnf(test, cons)), formula_neg),
                z3.And(original_neg, formula_pos, z3.And(stl_model_to_cnf(test, cons)))))
    return True if s.check() == z3.sat else False


def get_cons_enc(cons):
    """ Returns z3 instance for each string that declares a constant. """
    res = list()
    for c in list(set(cons)):
        name, form = c.strip(')').split(' ')[1:]
        if form == 'Bool':
            res.append(z3.Bool(name))
        elif form == 'Real':
            res.append(z3.Real(name))
    return res


def stl_model_to_cnf(model, aps):
    """ Converts a z3 model for a STL formula into a conjunctive normal form."""
    terms = list()
    for x in aps:
        value = model[x]
        if value is None: continue
        terms += [eq(x, value)]
    return terms


def initialize(formula):
    """ Generates mutants for a given formula and returns encoded formula,
    a list of Mutant-objects and the list of used constants."""

    mutated_formulae = list()
    mutant_dict = generate_mutants(formula, 0, 1)
    for x in mutant_dict:
        mutated_formulae += mutant_dict[x]
    mutated_formulae = list(set(mutated_formulae))

    f_nnf_pos = formula.expand().nextnormalform()
    f_nnf_neg = NOT(f_nnf_pos)
    (f_enc_pos, f_cons_pos) = f_nnf_pos.negationnormalform().encode()
    (f_enc_neg, f_cons_neg) = f_nnf_neg.negationnormalform().encode()
    z3f_pos = z3.parse_smt2_string(''.join([c for c in list(set(f_cons_pos))]) + '(assert ' + f_enc_pos + ')')
    z3f_neg = z3.parse_smt2_string(''.join([c for c in list(set(f_cons_neg))]) + '(assert ' + f_enc_neg + ')')

    pool_size = multiprocessing.cpu_count()
    pool = ThreadPool(pool_size)

    def encode_worker(m, mutants, constants):
        nnf_pos = m.expand().nextnormalform()
        nnf_neg = NOT(nnf_pos)
        enc_pos, cons_pos = nnf_pos.negationnormalform().encode()
        enc_neg, cons_neg = nnf_neg.negationnormalform().encode()
        z3string_pos = ''.join([c for c in list(set(cons_pos))]) + '(assert ' + enc_pos + ')'
        z3string_neg = ''.join([c for c in list(set(cons_neg))]) + '(assert ' + enc_neg + ')'
        m_cons = list(set(cons_pos + cons_neg))
        mutants.append(Mutant(None, m, z3string_pos, z3string_neg, m_cons))
        constants += m_cons

    mutants = list()
    constants = list()
    for m in mutated_formulae:
        pool.apply_async(encode_worker, (m, mutants, constants))

    pool.close()
    pool.join()

    for m in mutants:
        m.z3_pos = z3.parse_smt2_string(m.z3string_pos)
        m.z3_neg = z3.parse_smt2_string(m.z3string_neg)

    # Convert string representations of constants into z3 instances
    constants = list(set(constants + f_cons_pos + f_cons_neg))
    constants = get_cons_enc(constants)

    return z3f_pos, z3f_neg, mutants, constants


def check_kills(f_pos, f_neg, mutants, test, aps):
    """ Checks which mutants out of a given list get killed by a given test. """

    cnf = stl_model_to_cnf(test, aps)
    s = z3.Solver()
    count = 1  # Initialized with 1 due to mutant that was used to generate test
    for i in range(0, len(mutants)):
        m = mutants[i]
        if m.killed: continue
        s.push()
        s.add(z3.Or(z3.And(f_pos, z3.And(cnf), m.z3_neg), z3.And(f_neg, m.z3_pos, z3.And(cnf))))
        if s.check() == z3.sat:
            mutants[i].killed = True
            count += 1
        s.pop()
    return count


def generate_test(f_pos, f_neg, mutants, tests, aps, coverages):
    """
    Generates test for a given formula.

    Args:
        f_pos (z3 instance) : Positive Z3 representation of temporal logic formula for which tests are generated.
        f_neg (z3 instance) : Negative Z3 representation of temporal logic formula for which tests are generated.
        mutants (list) : List of Z3 encoded mutants of formula.
        tests (list) : List of tuples of already generated tests for the formula and their kind
        (whether they satisfy the original formula or not).
        aps (list) : List of Z3 instances of atomic propositions used in the formula and its mutants.
        coverages (list) : List of ints that each correspond to the percentage of mutants killed by the test at
        the same position in the list of tests.

    Returns:
        tuple : Tuple with positive and negative formulae, mutants and aps as above.
        Tests and coverages now also include the newly generated test.
    """

    def get_test(solver_input, alternative_input):
        t = None
        kind = None
        s = z3.Solver()
        s.push()
        s.add(solver_input)
        if s.check() == z3.sat:
            t = s.model()
            kind = True
        else:
            # If test cannot be generated with this solver input try alternative
            s.pop()
            s.push()
            s.add(alternative_input)
            if s.check() == z3.sat:
                t = s.model()
                kind = False
        return t, kind

    # Find first mutant in list that has not been killed yet
    m_index = -1
    m_pos = m_neg = None
    for i in range(0, len(mutants)):
        tmp = mutants[i]
        if not tmp.killed:
            m_pos = tmp.z3_pos
            m_neg = tmp.z3_neg
            mutants[i].killed = True
            m_index = i
            break

    # If all mutants were killed return None
    if m_index == -1:
        return None

    # Randomly generate positive or negative test
    if random.getrandbits(1):
        (t, kind) = get_test(z3.And(f_pos, m_neg), z3.And(f_neg, m_pos))  # Positive test if possible
    else:
        (t, kind) = get_test(z3.And(f_neg, m_pos), z3.And(f_pos, m_neg))  # Negative test if possible
        kind = not kind

    # If no test was generated proceed with next mutant
    if t is None:
        return generate_test(f_pos, f_neg, mutants, tests, aps, coverages)
    # Else return tuple with updated sets of tests and mutants
    else:
        tests.append(t)
        coverages.append(check_kills(f_pos, f_neg, mutants, t, aps))
        return f_pos, f_neg, mutants, tests, aps, coverages, kind


def get_plot_values(names_and_times, values):
    """ Gets plot values for each variable.

    Args:
        names_and_times (list) : The list of names for atomic
                                 propositions and the point in
                                 time they are evaluated in.
        values (list) : Contains the values for the atomic
                        proposition at the corresponding point in time.

    Returns:
        dict : Dictionary with one entry for each variable in the format of:
               dictionary[variable] = (points in time, corresponding values
               for each point in time, format(either Real or Bool))
    """

    def get_names(thelist):
        names = list()
        for (x, y) in thelist:
            if not (x in names):
                names.append(x)
        return names

    result = dict()
    for name in get_names(names_and_times):
        result[name] = (list(), list(),)  # Last entry of tuple: 0 for Reals, 1 for Boolean
        for i in range(0, len(names_and_times)):
            (n, t) = names_and_times[i]
            if n == name:
                result[name][0].append(t)
                result[name][1].append(values[i])
        if (not result[name][1] == []) and isinstance(result[name][1][0], (int, float, long)):
            result[name] += (0,)
        else:
            result[name] += (1,)
    return result


def get_xaxis_bounds(plotnums):
    """ Get longest xaxis bounds for the plot
    so that all subplots have the same xaxis.
    """
    lower = upper = 0
    for x in plotnums:
        times = plotnums[x][0]
        l, u = times[0], times[-1]
        if l < lower:
            lower = l
        if u > upper:
            upper = u
    return lower, upper


def guiformat(formula, t, aps):
    """
    Converts test into format that gui uses for display.

    Args:
        formula (Clause) : Formula to which the test belongs.
        t (z3 model) : Test to be converted.
        aps (z3 instances) : Variables of the atomic propositions used in test.

    Returns:
        dict : Dictionary in the format dict[variable] = [value_1 ... value_2] where for each time and
        interval point in between 0 and the length of the signal there is one value in the list of values.
    """
    pairs = list()
    for z in aps:
        v = t[z]
        if v is not None:
            if z3.is_rational_value(v):
                pairs += [(z, float(v.numerator_as_long()) / float(v.denominator_as_long()))]
            else:
                if z3.is_true(v):
                    pairs += [(z, True)]
                else:
                    pairs += [(z, False)]
    (names_and_times, values) = [(x, float(y)) for (x, y) in [a.__str__().split("___") for a, _ in pairs]], \
                                [x for (_, x) in pairs]
    plotnums = get_plot_values(names_and_times, values)

    # Arrange time points in increasing order but
    # with corresponding values in the same order
    for x in plotnums:
        tmp0 = plotnums[x][0]
        tmp1 = plotnums[x][1]
        plotnums[x] = (sorted(tmp0), list(), plotnums[x][2])
        for i in range(0, len(tmp0)):
            plotnums[x][1].append(tmp1[tmp0.index(plotnums[x][0][i])])
    lower_bound, upper_bound = get_xaxis_bounds(plotnums)

    # Fill values so that at every c/2 step there is one entry
    newtimes = [0.5 * x for x in range(2 * int(lower_bound), 2 * int(formula.length()) + 2)]
    gui = dict()
    for x in plotnums:
        times, values, kind = plotnums[x]
        count = 0
        newvalues = list()
        for time in newtimes:
            newvalues.append(values[count])
            if time in times and count < len(times) - 1:
                count += 1
        gui[x] = newvalues
    return gui

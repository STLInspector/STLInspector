from ..core.parsing import *
from ..core.testgeneration import *
from fractions import gcd

# represents one open project
class Project:
    # the id should be alphanumeric such that everything works fine
    # such as the usage of the id as css class
    # if data is given, the project is initialized with it
    def __init__(self, id, data={}):
        self.id = id
        self.title = data['title'] if 'title' in data else 'Untitled'
        self.stepWidth = data['stepWidth'] if 'stepWidth' in data else -1
        self.stlCandidate_text = data['stlCandidate_text'] if 'stlCandidate_text' in data else ''
        self.textRequirement = data['textRequirement'] if 'textRequirement' in data else ''
        self.textNotes = data['textNotes'] if 'textNotes' in data else ''
        self.tests = self.loadTests(data['tests']) if 'tests' in data else []
        self.kinds = data['kinds'] if 'kinds' in data else []
        self.coverages = data['coverages'] if 'coverages' in data else []
        self.visualInspection = data['visualInspection'] if 'visualInspection' in data else {}
        self.conflict = data['conflict'] if 'conflict' in data else False
        self.mutants = [Mutant(dictionary=m) for m in data['mutants']] if 'mutants' in data and data['mutants'] != None else None
        self.constants = self.loadConstants() if 'mutants' in data and data['mutants'] != None else None
        self.stlCandidate = self.loadFormula() if 'stlCandidate_text' in data and data['stlCandidate_text'] != '' else None
        (z3f_pos, z3f_neg) = self.loadZ3Formula() if 'stlCandidate_text' in data and data['stlCandidate_text'] != '' else (None, None)
        self.z3f_pos = z3f_pos
        self.z3f_neg = z3f_neg

    def loadZ3Formula(self):
        nnf_pos = self.stlCandidate.expand().nextnormalform()
        nnf_neg = NOT(nnf_pos)
        (enc_pos, cons_pos) = nnf_pos.negationnormalform().encode()
        (enc_neg, cons_neg) = nnf_neg.negationnormalform().encode()
        pos = z3.parse_smt2_string(''.join([c for c in list(set(cons_pos))])+'(assert '+enc_pos+')')
        neg = z3.parse_smt2_string(''.join([c for c in list(set(cons_neg))])+'(assert '+enc_neg+')')
        return (pos, neg)

    def loadFormula(self):
        tmp = parse(self.stlCandidate_text)
        return tmp.adjust(self.stepWidth)

    # loads all constants used for tests from mutants
    def loadConstants(self):
        constantstrings = list()
        for m in self.mutants:
            constantstrings += m.cons_strings
        return get_cons_enc(constantstrings) # uses method from solver.py

    # converts saved tests back into z3 format        
    def loadTests(self, tuples):
        def tuplesToConjunction(theTuples):
            def helper(t):
                if len(t) == 1:
                    if isinstance(t[0][1], bool):
                        return '(= {} {})'.format(t[0][0], t[0][1].__str__().lower())
                    else:
                        return '(= {} {})'.format(t[0][0], t[0][1])
                else:
                    if isinstance(t[0][1], bool):
                        return '(and (= {} {}) {})'.format(t[0][0], t[0][1].__str__().lower(), helper(t[1:]))
                    else:
                        return '(and (= {} {}) {})'.format(t[0][0], t[0][1], helper(t[1:]))
            constants = list()
            for name, value in theTuples:
                if isinstance(value, bool):
                    constants.append('(declare-const {} Bool)'.format(name))
                else:
                    constants.append('(declare-const {} Real)'.format(name))
            return ''.join([c for c in list(set(constants))])+'(assert '+helper(theTuples)+')'
        tests = list()
        s = z3.Solver()
        for t in tuples:
            conjunction = tuplesToConjunction(t)
            s.push()
            s.add(z3.parse_smt2_string(conjunction))
            if s.check() == z3.sat:
                tests.append(s.model())
            s.pop()
        return tests

    def setTitle(self, title):
        self.title = title

    # calculates the step width that will be used for a given formula
    def getStepWidth(self, f):
        limits = f.getLimits()
        return 1 if limits == [] else reduce(gcd, limits)

    # returns the highest amount of tests that have been evaluated by one single user
    def furthestEvaluation(self):
        res = -1
        for x in self.visualInspection:
            if len(self.visualInspection[x]) > res:
                res = len(self.visualInspection[x])
        return res

    def overview(self):
        if self.mutants == None or len(self.mutants) == 0:
            coverage = 0
        else:
            coverage = sum(self.coverages[:self.furthestEvaluation()])/float(len(self.mutants))*100
        return {
            'id': self.id,
            'title': self.title,
            'coverage': coverage,
            'conflict': self.conflict
        }

    # overwrites the current stlCandidate
    # param stlCandidate_text stlCandidate in text representation
    # if stlCandidate_text cannot be parsed, an exception is raised
    def setStlCandidate(self, stlCandidate_text):
        try:
            formula = parse(stlCandidate_text)
            self.stlCandidate_text = formula.__str__()
            self.stepWidth = self.getStepWidth(formula)
            self.stlCandidate = formula.adjust(self.stepWidth)
            (self.z3f_pos, self.z3f_neg, self.mutants, self.constants) = initialize(self.stlCandidate)
            self.tests = list()
            self.kinds = list()
            self.coverages = list()
            self.visualInspection = dict()
            self.conflict = False
        except Exception as err:
            print "error: {}".format(err)
            raise Exception('Could not parse stl formula')

    # set the textRequirement
    # param textRequirement
    def setTextRequirement(self, textRequirement):
        self.textRequirement = textRequirement

    # set the textNotes
    # param textNotes
    def setTextNotes(self, textNotes):
        self.textNotes = textNotes

    # returns the project state
    def state(self):
        if self.mutants == None or len(self.mutants) == 0:
            coverage = 0
        else:
            coverage = sum(self.coverages[:self.furthestEvaluation()])/float(len(self.mutants))*100
        return {
            'id': self.id,
            'title': self.title,
            'coverage': coverage,
            'textRequirement': self.textRequirement,
            'stlCandidate': self.stlCandidate_text,
            'textNotes': self.textNotes,
            'testCount': len(self.tests),
            'sat': {
                'candidate': self.kinds,
                'visualInspection': self.visualInspection
            },
            'conflict': self.conflict
        }

    def saveTests(self):
        testtuples = list()
        for t in self.tests:
            currenttest = list()
            for c in self.constants:
                value = t[c]
                if not value == None:
                    if z3.is_rational_value(value):
                        currenttest += [(c.__str__(), float(value.numerator_as_long())/float(value.denominator_as_long()))]
                    else:
                        if z3.is_true(value):
                            currenttest += [(c.__str__(), True)]
                        else:
                            currenttest += [(c.__str__(), False)]
            testtuples.append(currenttest)
        return testtuples

    # returns the data of the project for saving into a file etc.
    def save(self):
        return {
            'title': self.title,
            'stepWidth': self.stepWidth,
            'stlCandidate_text': self.stlCandidate_text,
            'textRequirement': self.textRequirement,
            'textNotes': self.textNotes,
            'tests': self.saveTests(),
            'kinds': self.kinds,
            'coverages': self.coverages,
            'visualInspection': self.visualInspection,
            'conflict': self.conflict,
            'mutants': [m.serialize() for m in self.mutants] if self.mutants != None else None
        }

    # returns already existing
    # test of given id
    def testById(self, id):
        return {
            'finished': False,
            'coverage': sum(self.coverages[:self.furthestEvaluation()])/float(len(self.mutants))*100,
            'testId': id, 
            'kind': self.kinds[id],
            'step': self.stepWidth,
            'signals': guiformat(self.stlCandidate, self.tests[id], self.constants),
            'conflict': self.conflict
        }

    # if the user has not evaluated
    # all existing tests, then the
    # next not yet evaluated test
    # is returned. Otherwise, a new
    # test is generated and returned.
    def testForName(self, name):
        if not name in self.visualInspection:
            self.visualInspection[name] = list()
        userEvaluation = self.visualInspection[name]
        if (len(userEvaluation) < len(self.tests)):
            # user has not evaluated all existing tests
            if len(userEvaluation) == 0:
                coverage = 0
            else:
                coverage = sum(self.coverages[:len(userEvaluation)])/float(len(self.mutants))*100
            return {
                'finished': False,
                'coverage': coverage,
                'testId': len(userEvaluation), 
                'kind': self.kinds[len(userEvaluation)],
                'step': self.stepWidth,
                'signals': guiformat(self.stlCandidate, self.tests[len(userEvaluation)], self.constants),
                'conflict': self.conflict
            }
        else:
            res = generate_test(self.z3f_pos, self.z3f_neg, self.mutants, self.tests, self.constants, self.coverages)
            if res == None:
                self.coverages[-1] = len(self.mutants) - (sum(self.coverages) - self.coverages[-1])
                # no new tests can be generated
                return {
                    'finished': True,
                    'coverage': sum(self.coverages)/float(len(self.mutants))*100,
                    'conflict': self.conflict
                }
            else:
                (self.z3f_pos, self.z3f_neg, self.mutants, self.tests, self.constants, self.coverages, kind) = res
                self.kinds.append(kind)
                return {
                    'finished': False,
                    'coverage': sum(self.coverages[:-1])/float(len(self.mutants))*100,
                    'testId': len(self.tests)-1,
                    'kind': self.kinds[-1],
                    'step': self.stepWidth,
                    'signals': guiformat(self.stlCandidate, self.tests[-1], self.constants),
                    'conflict': self.conflict
                }

    # saves evaluation result of user and
    # returns true iff user correctly classified test
    def setTestEvaluation(self, id, name, evaluation):
        userEvaluation = self.visualInspection[name]
        if len(userEvaluation) <= id:
            self.visualInspection[name].append(evaluation)
        else:
            self.visualInspection[name][id] = evaluation
        self.conflict = True if self.conflict else (evaluation != self.kinds[id])
        return self.kinds[id] == evaluation


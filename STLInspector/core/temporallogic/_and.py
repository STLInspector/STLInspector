from clause import *


class AND(Clause):
    """
    This class represents the logical operation 'and'.
    
    Attributes:
        operand1 (Clause) : First operand of this binary logical expression.
        operand2 (Clause) : Second operand of this binary logical expression.

    Clause attributes that are set: namestring (str) : String "&" used for printing.

    Examples:
        AND(AP("a"), AP("b")) - a & b
        AND(AP("a"), AND(AP("b"), AP("c"))) - a & (b & c)
        AND(NOT(AP("a")), OR(AP("b"), AP("c"))) - (!a) & (b | c)
    """

    def __init__(self, operand1, operand2):
        Clause.__init__(self, "&", operand1, operand2)

    # Overwrites method of class Clause
    def __eq__(self, other):
        return isinstance(other, AND) \
               and ((other.operand1 == self.operand1 and other.operand2 == self.operand2)
                    or (other.operand1 == self.operand2 and other.operand2 == self.operand1))

    def length(self):
        """ Calculates the length (number of time steps) of a given formula. """
        return max(self.operand1.length(), self.operand2.length())

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        return AND(self.operand1.adjust(c), self.operand2.adjust(c))

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        return self.operand1.getLimits() + self.operand2.getLimits()

    @remove_duplicates
    def aso(self):
        from _or import OR
        from implies import IMPLIES
        from until import UNTIL
        from release import RELEASE
        from _finally import FINALLY
        from globally import GLOBALLY
        from next import NEXT
        result = list()
        if isinstance(self.operand1, (AND, OR, IMPLIES)) and not isinstance(self.operand1, AND):
            result += [self.operand1.__class__(self.operand1.operand1, AND(self.operand1.operand2, self.operand2))]
        if isinstance(self.operand2, (AND, OR, IMPLIES)) and not isinstance(self.operand2, AND):
            result += [self.operand2.__class__(AND(self.operand1, self.operand2.operand1), self.operand2.operand2)]
        if isinstance(self.operand1, (UNTIL, RELEASE)):
            result += [self.operand1.__class__(self.operand1.operand1, AND(self.operand1.operand2, self.operand2),
                                               self.operand1.lower_bound, self.operand1.upper_bound)]
        if isinstance(self.operand2, (UNTIL, RELEASE)):
            result += [self.operand2.__class__(AND(self.operand1, self.operand2.operand1), self.operand2.operand2,
                                               self.operand2.lower_bound, self.operand2.upper_bound)]
        if isinstance(self.operand1, (FINALLY, GLOBALLY)):
            result += [self.operand1.__class__(AND(self.operand1.operand1, self.operand2), self.operand1.lower_bound,
                                               self.operand1.upper_bound)]
        if isinstance(self.operand2, (FINALLY, GLOBALLY)):
            result += [self.operand2.__class__(AND(self.operand1, self.operand2.operand1), self.operand2.lower_bound,
                                               self.operand2.upper_bound)]
        if isinstance(self.operand1, NEXT):
            result += [NEXT(AND(self.operand1.operand1, self.operand2), self.operand1.lower_bound)]
        if isinstance(self.operand2, NEXT):
            result += [NEXT(AND(self.operand1, self.operand2.operand1), self.operand2.lower_bound)]
        return result + [AND(y, self.operand2) for y in self.operand1.aso() if not y == self.operand2] \
               + [AND(self.operand1, y) for y in self.operand2.aso() if not y == self.operand1]

    @remove_duplicates
    def mto(self):
        return [AND(y, self.operand2) for y in self.operand1.mto()] \
               + [AND(self.operand1, y) for y in self.operand2.mto()]

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        from _finally import FINALLY
        from globally import GLOBALLY
        from next import NEXT
        return [AND(FINALLY(self.operand1, lower_bound, upper_bound), self.operand2),
                    AND(self.operand1, FINALLY(self.operand2, lower_bound, upper_bound)),
                    AND(GLOBALLY(self.operand1, lower_bound, upper_bound), self.operand2),
                    AND(self.operand1, GLOBALLY(self.operand2, lower_bound, upper_bound)),
                    AND(NEXT(self.operand1, upper_bound), self.operand2),
                    AND(self.operand1, NEXT(self.operand2, upper_bound))] \
               + [AND(y, self.operand2) for y in self.operand1.tio(lower_bound, upper_bound) if not y == self.operand2] \
               + [AND(self.operand1, y) for y in self.operand2.tio(lower_bound, upper_bound) if not y == self.operand1]

    @remove_duplicates
    def ano(self):
        return [AND(y, self.operand2) for y in self.operand1.ano() if not y == self.operand2] \
               + [AND(self.operand1, y) for y in self.operand2.ano() if not y == self.operand1]

    @remove_duplicates
    def oro(self, atomic_props):
        return [AND(y, self.operand2) for y in self.operand1.oro(atomic_props) if not y == self.operand2] \
               + [AND(self.operand1, y) for y in self.operand2.oro(atomic_props) if not y == self.operand1]

    @remove_duplicates
    def lro(self):
        from _or import OR
        from implies import IMPLIES
        return [OR(self.operand1, self.operand2), OR(self.operand1, self.operand2),
                IMPLIES(self.operand1, self.operand2), IMPLIES(self.operand1, self.operand2)] \
               + [AND(y, self.operand2) for y in self.operand1.lro() if not y == self.operand2] \
               + [AND(self.operand1, y) for y in self.operand2.lro() if not y == self.operand1]

    @remove_duplicates
    def tro(self):
        return [AND(y, self.operand2) for y in self.operand1.tro() if not y == self.operand2] \
               + [AND(self.operand1, y) for y in self.operand2.tro() if not y == self.operand1]

    @remove_duplicates
    def io(self):
        return [AND(y, self.operand2) for y in self.operand1.io() if not y == self.operand2] \
               + [AND(self.operand1, y) for y in self.operand2.io() if not y == self.operand1]

    @remove_duplicates
    def eno(self):
        from _not import NOT
        return [NOT(self)] + [AND(y, self.operand2) for y in self.operand1.eno()] \
               + [AND(self.operand1, y) for y in self.operand2.eno()]

    @remove_duplicates
    def rro(self):
        return [AND(y, self.operand2) for y in self.operand1.rro() if not y == self.operand2] \
               + [AND(self.operand1, y) for y in self.operand2.rro() if not y == self.operand1]

    @remove_duplicates
    def mco(self):
        from ap import AP
        result = list()
        if isinstance(self.operand1, AP):
            result += [self.operand2] + [AND(y, self.operand2) for y in self.operand1.mco()] \
                      + [AND(self.operand1, y) for y in self.operand2.mco()]
        if isinstance(self.operand2, AP):
            result += [self.operand1] + [AND(y, self.operand2) for y in self.operand1.mco()] \
                      + [AND(self.operand1, y) for y in self.operand2.mco()]
        if not (isinstance(self.operand1, AP) or isinstance(self.operand2, AP)):
            result += [AND(y, self.operand2) for y in self.operand1.mco()] \
                      + [AND(self.operand1, y) for y in self.operand2.mco()]
        return result

    @remove_duplicates
    def sto(self, onezero):
        return [AND(y, self.operand2) for y in self.operand1.sto(onezero) if not y == self.operand2] \
               + [AND(self.operand1, y) for y in self.operand2.sto(onezero) if not y == self.operand1]

    def ufc_plus(self):
        return [AND(y, self.operand2) for y in self.operand1.ufc_plus()] \
               + [AND(self.operand1, y) for y in self.operand2.ufc_plus()]

    def ufc_minus(self):
        return [AND(y, self.operand2) for y in self.operand1.ufc_minus()] \
                + [AND(self.operand1, y) for y in self.operand2.ufc_minus()]
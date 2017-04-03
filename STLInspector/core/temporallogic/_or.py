from clause import *


class OR(Clause):
    """
    This class represents the logical operation 'or'.
    
    Attributes:
        operand1 (Clause) : First operand of this binary logical expression.
        operand2 (Clause) : Second operand of this binary logical expression.
        
    Clause attributes that are set: namestring (str) : String "|" used for printing.
    
    Examples:
        Or(AP("a"), AP("b")) - a | b
        OR(AP("a"), OR(AP("b"), AP("c"))) - a | (b | c)
        OR(NOT(AP("a")), AND(AP("b"), AP("c"))) - (!a) | (b & c)
    """
    
    def __init__(self, operand1, operand2):
        Clause.__init__(self, "|", operand1, operand2)

    # Overwrites method of class Clause
    def __eq__(self, other):
        return isinstance(other, OR)\
               and ((other.operand1 == self.operand1 and other.operand2 == self.operand2)
                    or (other.operand1 == self.operand2 and other.operand2 == self.operand1))

    def length(self):
        """ Calculates the length (number of time steps) of a given formula. """
        return max(self.operand1.length(), self.operand2.length())

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        return OR(self.operand1.adjust(c), self.operand2.adjust(c))

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        return self.operand1.getLimits() + self.operand2.getLimits()

    @remove_duplicates
    def aso(self):
        from _and import AND
        from implies import IMPLIES
        from until import UNTIL
        from release import RELEASE
        from _finally import FINALLY
        from globally import GLOBALLY
        from next import NEXT
        result = list()
        if isinstance(self.operand1, (AND, OR, IMPLIES)) and not isinstance(self.operand1, OR):
            result += [self.operand1.__class__(self.operand1.operand1, OR(self.operand1.operand2, self.operand2))]
        if isinstance(self.operand2, (AND, OR, IMPLIES)) and not isinstance(self.operand2, OR):
            result += [
                self.operand2.__class__(self.__class__(self.operand1, self.operand2.operand1), self.operand2.operand2)]
        if isinstance(self.operand1, (UNTIL, RELEASE)):
            result += [self.operand1.__class__(self.operand1.operand1, OR(self.operand1.operand2, self.operand2),
                                               self.operand1.lower_bound, self.operand1.upper_bound)]
        if isinstance(self.operand2, (UNTIL, RELEASE)):
            result += [
                self.operand2.__class__(self.__class__(self.operand1, self.operand2.operand1), self.operand2.operand2,
                                        self.operand2.lower_bound, self.operand2.upper_bound)]
        if isinstance(self.operand1, (FINALLY, GLOBALLY)):
            result += [self.operand1.__class__(self.__class__(self.operand1.operand1, self.operand2),
                                               self.operand1.lower_bound,
                                               self.operand1.upper_bound)]
        if isinstance(self.operand2, (FINALLY, GLOBALLY)):
            result += [self.operand2.__class__(self.__class__(self.operand1, self.operand2.operand1),
                                               self.operand2.lower_bound,
                                               self.operand2.upper_bound)]
        if isinstance(self.operand1, NEXT):
            result += [NEXT(self.__class__(self.operand1.operand1, self.operand2), self.operand1.lower_bound)]
        if isinstance(self.operand2, NEXT):
            result += [NEXT(self.__class__(self.operand1, self.operand2.operand1), self.operand2.lower_bound)]
        return result + [OR(y, self.operand2) for y in self.operand1.aso() if not y == self.operand2] \
               + [OR(self.operand1, y) for y in self.operand2.aso() if not y == self.operand1]

    @remove_duplicates
    def mto(self):
        return [OR(y, self.operand2) for y in self.operand1.mto()] \
               + [OR(self.operand1, y) for y in self.operand2.mto()]

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        from _finally import FINALLY
        from globally import GLOBALLY
        from next import NEXT
        return [OR(FINALLY(self.operand1, lower_bound, upper_bound), self.operand2),
                OR(self.operand1, FINALLY(self.operand2, lower_bound, upper_bound)),
                OR(GLOBALLY(self.operand1, lower_bound, upper_bound), self.operand2),
                OR(self.operand1, GLOBALLY(self.operand2, lower_bound, upper_bound)),
                OR(NEXT(self.operand1, upper_bound), self.operand2),
                OR(self.operand1, NEXT(self.operand2, upper_bound))] \
               + [OR(y, self.operand2) for y in self.operand1.tio(lower_bound, upper_bound) if not y == self.operand2] \
               + [OR(self.operand1, y) for y in self.operand2.tio(lower_bound, upper_bound) if not y == self.operand1]

    @remove_duplicates
    def ano(self):
        return [OR(y, self.operand2) for y in self.operand1.ano() if not y == self.operand2] \
               + [OR(self.operand1, y) for y in self.operand2.ano() if not y == self.operand1]

    @remove_duplicates
    def oro(self, atomic_props):
        return [OR(y, self.operand2) for y in self.operand1.oro(atomic_props) if not y == self.operand2] \
               + [OR(self.operand1, y) for y in self.operand2.oro(atomic_props) if not y == self.operand1]

    @remove_duplicates
    def lro(self):
        from _and import AND
        from implies import IMPLIES
        return [AND(self.operand1, self.operand2), AND(self.operand1, self.operand2),
                IMPLIES(self.operand1, self.operand2), IMPLIES(self.operand1, self.operand2)] \
               + [OR(y, self.operand2) for y in self.operand1.lro() if not y == self.operand2] \
               + [OR(self.operand1, y) for y in self.operand2.lro() if not y == self.operand1]

    @remove_duplicates
    def tro(self):
        return [OR(y, self.operand2) for y in self.operand1.tro() if not y == self.operand2] \
               + [OR(self.operand1, y) for y in self.operand2.tro() if not y == self.operand1]

    @remove_duplicates
    def io(self):
        return [OR(y, self.operand2) for y in self.operand1.io() if not y == self.operand2] \
               + [OR(self.operand1, y) for y in self.operand2.io() if not y == self.operand1]

    @remove_duplicates
    def eno(self):
        from _not import NOT
        return [NOT(self)] + [OR(y, self.operand2) for y in self.operand1.eno()] \
               + [OR(self.operand1, y) for y in self.operand2.eno()]

    @remove_duplicates
    def rro(self):
        return [OR(y, self.operand2) for y in self.operand1.rro() if not y == self.operand2] \
               + [OR(self.operand1, y) for y in self.operand2.rro() if not y == self.operand1]

    @remove_duplicates
    def mco(self):
        from ap import AP
        result = list()
        if isinstance(self.operand1, AP):
            result += [self.operand2] + [OR(y, self.operand2) for y in self.operand1.mco()] \
                      + [OR(self.operand1, y) for y in self.operand2.mco()]
        if isinstance(self.operand2, AP):
            result += [self.operand1] + [OR(y, self.operand2) for y in self.operand1.mco()] \
                      + [OR(self.operand1, y) for y in self.operand2.mco()]
        if not (isinstance(self.operand1, AP) or isinstance(self.operand2, AP)):
            result += [OR(y, self.operand2) for y in self.operand1.mco()] \
                      + [OR(self.operand1, y) for y in self.operand2.mco()]
        return result

    @remove_duplicates
    def sto(self, onezero):
        return [OR(y, self.operand2) for y in self.operand1.sto(onezero) if not y == self.operand2] \
               + [OR(self.operand1, y) for y in self.operand2.sto(onezero) if not y == self.operand1]

    def ufc_plus(self):
        from _and import AND
        from _not import NOT
        return [AND(y, NOT(self.operand2)) for y in self.operand1.ufc_plus()] \
               + [AND(NOT(self.operand1), y) for y in self.operand2.ufc_plus()]

    def ufc_minus(self):
        from _and import AND
        from _not import NOT
        return [AND(y, NOT(self.operand2)) for y in self.operand1.ufc_minus()] \
               + [AND(NOT(self.operand1), y) for y in self.operand2.ufc_minus()]

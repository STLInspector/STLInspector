from clause import *


class IMPLIES(Clause):
    """
    This class represents the logical operation 'implies'.
    
    Attributes:
        operand1 (Clause) : First operand of this binary logical expression.
        operand2 (Clause) : Second operand of this binary logical expression.

    Clause attributes that are set: namestring (str) : String "->" used for printing.
    
    Examples:
        IMPLIES(AP("a"), AP("b")) - a -> b
        IMPLIES(AP("a"), IMPLIES(AP("b"), AP("c"))) - a -> (b -> c)
        IMPLIES(NOT(AP("a")), AND(AP("b"), AP("c"))) - (!a) -> (b & c)
    """
    
    def __init__(self, operand1, operand2):
        Clause.__init__(self, "->", operand1, operand2)
    
    # Overwrites method of class Clause
    def __eq__(self, other):
        if isinstance(other, IMPLIES) \
                and other.operand1 == self.operand1 \
                and other.operand2 == self.operand2:
            return True
        else:
            return False
        
    # Overwrites method of class Clause
    def negationnormalform(self):
        from _or import OR
        from _not import NOT
        return OR(NOT(self.operand1), self.operand2).negationnormalform()

    def length(self):
        """ Calculates the length (number of time steps) of a given formula. """
        return max(self.operand1.length(), self.operand2.length())

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        return IMPLIES(self.operand1.adjust(c), self.operand2.adjust(c))

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        return self.operand1.getLimits() + self.operand2.getLimits()

    @remove_duplicates
    def aso(self):
        from _and import AND
        from _or import OR
        from until import UNTIL
        from release import RELEASE
        from _finally import FINALLY
        from globally import GLOBALLY
        from next import NEXT
        result = list()
        if isinstance(self.operand1, (AND, OR, IMPLIES)) and not isinstance(self.operand1, IMPLIES):
            result += [self.operand1.__class__(self.operand1.operand1, IMPLIES(self.operand1.operand2, self.operand2))]
        if isinstance(self.operand2, (AND, OR, IMPLIES)) and not isinstance(self.operand2, IMPLIES):
            result += [self.operand2.__class__(IMPLIES(self.operand1, self.operand2.operand1), self.operand2.operand2)]
        if isinstance(self.operand1, (UNTIL, RELEASE)):
            result += [self.operand1.__class__(self.operand1.operand1, IMPLIES(self.operand1.operand2, self.operand2),
                                               self.operand1.lower_bound, self.operand1.upper_bound)]
        if isinstance(self.operand2, (UNTIL, RELEASE)):
            result += [self.operand2.__class__(IMPLIES(self.operand1, self.operand2.operand1), self.operand2.operand2,
                                               self.operand2.lower_bound, self.operand2.upper_bound)]
        if isinstance(self.operand1, (FINALLY, GLOBALLY)):
            result += [self.operand1.__class__(IMPLIES(self.operand1.operand1, self.operand2),
                                               self.operand1.lower_bound, self.operand1.upper_bound)]
        if isinstance(self.operand2, (FINALLY, GLOBALLY)):
            result += [self.operand2.__class__(IMPLIES(self.operand1, self.operand2.operand1),
                                               self.operand2.lower_bound, self.operand2.upper_bound)]
        if isinstance(self.operand1, NEXT):
            result += [NEXT(IMPLIES(self.operand1.operand1, self.operand2), self.operand1.lower_bound)]
        if isinstance(self.operand2, NEXT):
            result += [NEXT(IMPLIES(self.operand1, self.operand2.operand1), self.operand2.lower_bound)]
        return result + [IMPLIES(y, self.operand2) for y in self.operand1.aso() if not y == self.operand2] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.aso() if not y == self.operand1]

    @remove_duplicates
    def mto(self):
        return [IMPLIES(y, self.operand2) for y in self.operand1.mto()] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.mto()]

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        from _finally import FINALLY
        from globally import GLOBALLY
        from next import NEXT
        return [IMPLIES(FINALLY(self.operand1, lower_bound, upper_bound), self.operand2),
                    IMPLIES(self.operand1, FINALLY(self.operand2, lower_bound, upper_bound)),
                    IMPLIES(GLOBALLY(self.operand1, lower_bound, upper_bound), self.operand2),
                    IMPLIES(self.operand1, GLOBALLY(self.operand2, lower_bound, upper_bound)),
                    IMPLIES(NEXT(self.operand1, upper_bound), self.operand2),
                    IMPLIES(self.operand1, NEXT(self.operand2, upper_bound))] \
               + [IMPLIES(y, self.operand2) for y in self.operand1.tio(lower_bound, upper_bound)
                  if not y == self.operand2] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.tio(lower_bound, upper_bound)
                  if not y == self.operand1]

    @remove_duplicates
    def ano(self):
        return [IMPLIES(y, self.operand2) for y in self.operand1.ano() if not y == self.operand2] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.ano() if not y == self.operand1]

    @remove_duplicates
    def oro(self, atomic_props):
        return [IMPLIES(y, self.operand2) for y in self.operand1.oro(atomic_props) if not y == self.operand2] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.oro(atomic_props) if not y == self.operand1]

    @remove_duplicates
    def lro(self):
        from _or import OR
        from _and import AND
        return [OR(self.operand1, self.operand2), OR(self.operand1, self.operand2),
                AND(self.operand1, self.operand2), AND(self.operand1, self.operand2)] \
               + [IMPLIES(y, self.operand2) for y in self.operand1.lro() if not y == self.operand2] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.lro() if not y == self.operand1]

    @remove_duplicates
    def tro(self):
        return [IMPLIES(y, self.operand2) for y in self.operand1.tro() if not y == self.operand2] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.tro() if not y == self.operand1]

    @remove_duplicates
    def io(self):
        return [IMPLIES(y, self.operand2) for y in self.operand1.io() if not y == self.operand2] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.io() if not y == self.operand1]

    @remove_duplicates
    def eno(self):
        from _not import NOT
        return [NOT(self)] + [IMPLIES(y, self.operand2) for y in self.operand1.eno()] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.eno()]

    @remove_duplicates
    def rro(self):
        return [IMPLIES(y, self.operand2) for y in self.operand1.rro() if not y == self.operand2] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.rro() if not y == self.operand1]

    @remove_duplicates
    def mco(self):
        from ap import AP
        result = list()
        if isinstance(self.operand1, AP):
            result += [y for y in self.operand2.mco()]
        return result + [IMPLIES(y, self.operand2) for y in self.operand1.mco()] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.mco()]

    @remove_duplicates
    def sto(self, onezero):
        return [IMPLIES(y, self.operand2) for y in self.operand1.sto(onezero) if not y == self.operand2] \
               + [IMPLIES(self.operand1, y) for y in self.operand2.sto(onezero) if not y == self.operand1]

    def ufc_plus(self):
        from _or import OR
        from _not import NOT
        return OR(NOT(self.operand1), self.operand2).ufc_plus()

    def ufc_minus(self):
        from _or import OR
        from _not import NOT
        return OR(NOT(self.operand1), self.operand2).ufc_minus()

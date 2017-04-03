from clause import *


class RELEASE(Clause):
    """
    This class represents the temporal logic operation 'release'.
    
    The class can be used for both STL and LTL Release-operators.
    When it is used for LTL the interval bounds are simply set to None.
    
    Attributes:
        operand1 (Clause) : First operand of this binary temporal logic expression.
        operand2 (Clause) : Second operand of this binary temporal logic expression.
        lower_bound (int) : Lower boundary for STL interval.
        upper_bound (int) : Upper boundary for STL interval.

    Clause attributes that are set: namestring (str) : String "R" used for printing.
        
    Examples:
        RELEASE(AP("a"), AP("b")) - a R b
        RELEASE(AP("a"), FINALLY(AP("b"), 1, 2), 3, 4) - a R[3,4] (F[1,2] b)
        RELEASE(AP("a"), OR(AP("b"), RELEASE(AP("c"), AP("d")))) - a R (b | (c R d))
    """
    
    def __init__(self, operand1, operand2, lower_bound=None, upper_bound=None):
        Clause.__init__(self, "R", operand1, operand2, lower_bound, upper_bound)   
    
    # Overwrites method of class Clause        
    def expand(self):
        from _not import NOT
        from until import UNTIL
        return NOT(UNTIL(NOT(self.operand1.expand()), NOT(self.operand2.expand()), self.lower_bound, self.upper_bound))
    
    # Overwrites method of class Clause
    # Does not need a negationnormalform since its rewritten as Until beforehand
    def negationnormalform(self):
        pass

    # Overwrites method of class Clause      
    # Does not need a nextnormalform function since its rewritten as Until beforehand
    def nextnormalform(self, ininterval=0):
        pass
    
    # Overwrites method of class Clause      
    # Does not need a encode function since its rewritten as Until/Next beforehand
    def encode(self, state=0):
        pass

    def length(self):
        """ Calculates the length (number of time steps) of a given formula. """
        return max(self.operand1.length(), self.operand2.length()) + self.upper_bound

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        return RELEASE(self.operand1.adjust(c), self.operand2.adjust(c),
                       self.lower_bound / float(c), self.upper_bound / float(c))

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        return self.operand1.getLimits() + self.operand2.getLimits() + [self.lower_bound, self.upper_bound]

    @remove_duplicates
    def aso(self):
        from until import UNTIL
        from _and import AND
        from _or import OR
        from implies import IMPLIES
        from _finally import FINALLY
        from globally import GLOBALLY
        from next import NEXT
        result = list()
        if isinstance(self.operand1, (UNTIL, RELEASE)):
            result += [self.operand1.__class__(self.operand1.operand1,
                       RELEASE(self.operand1.operand2, self.operand2, self.lower_bound, self.upper_bound),
                       self.operand1.lower_bound, self.operand1.upper_bound)]
        if isinstance(self.operand2, (UNTIL, RELEASE)):
            result += [self.operand2.__class__(RELEASE(self.operand1, self.operand2.operand1,
                                                       self.lower_bound, self.upper_bound),
                       self.operand2.operand2, self.operand2.lower_bound, self.operand2.upper_bound)]
        if isinstance(self.operand1, (AND, OR, IMPLIES)):
            result += [self.operand1.__class__(self.operand1.operand1,
                                               RELEASE(self.operand1.operand2, self.operand2,
                                                       self.lower_bound, self.upper_bound))]
        if isinstance(self.operand2, (AND, OR, IMPLIES)):
            result += [self.operand2.__class__(RELEASE(self.operand1, self.operand2.operand1,
                                                       self.lower_bound, self.upper_bound), self.operand2.operand2)]
        if isinstance(self.operand1, (FINALLY, GLOBALLY)):
            result += [self.operand1.__class__(RELEASE(self.operand1.operand1, self.operand2,
                                                       self.lower_bound, self.upper_bound),
                       self.operand1.lower_bound, self.operand1.upper_bound)]
        if isinstance(self.operand2, (FINALLY, GLOBALLY)):
            result += [self.operand2.__class__(RELEASE(self.operand1, self.operand2.operand1,
                                                       self.lower_bound, self.upper_bound),
                       self.operand2.lower_bound, self.operand2.upper_bound)]
        if isinstance(self.operand1, NEXT):
            result += [NEXT(RELEASE(self.operand1.operand1, self.operand2, self.lower_bound, self.upper_bound),
                            self.operand1.lower_bound)]
        if isinstance(self.operand2, NEXT):
            result += [NEXT(RELEASE(self.operand1, self.operand2.operand1, self.lower_bound, self.upper_bound),
                            self.operand2.lower_bound)]
        return result + [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound)
                         for y in self.operand1.aso() if not y == self.operand2] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.aso() if not y == self.operand1]

    @remove_duplicates
    def mto(self):
        return [self.operand1, self.operand2] \
               + [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound) for y in self.operand1.mto()] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound) for y in self.operand2.mto()]

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        return [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.tio(lower_bound, upper_bound) if not y == self.operand2] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.tio(lower_bound, upper_bound) if not y == self.operand1]

    @remove_duplicates
    def ano(self):
        return [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.ano() if not y == self.operand2] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.ano() if not y == self.operand1]

    @remove_duplicates
    def oro(self, atomic_props):
        return [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.oro(atomic_props) if not y == self.operand2] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.oro(atomic_props) if not y == self.operand1]

    @remove_duplicates
    def lro(self):
        return [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.lro() if not y == self.operand2] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.lro() if not y == self.operand1]

    @remove_duplicates
    def tro(self):
        from until import UNTIL
        return [UNTIL(self.operand1, self.operand2, self.lower_bound, self.upper_bound)] \
               + [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound)
                  for y in self.operand1.tro() if not y == self.operand2] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.tro() if not y == self.operand1]

    @remove_duplicates
    def io(self):
        return [RELEASE(self.operand1, self.operand2, self.lower_bound + 1, self.upper_bound),
                RELEASE(self.operand1, self.operand2, self.lower_bound, self.upper_bound + 1),
                RELEASE(self.operand1, self.operand2, self.lower_bound, self.upper_bound - 1)] \
               + [RELEASE(self.operand1, self.operand2, self.lower_bound - 1, self.upper_bound)
                  for fake_iterator in [1] if not self.lower_bound == 0] \
               + [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound) for y in self.operand1.io()] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound) for y in self.operand2.io()]

    @remove_duplicates
    def eno(self):
        return [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound) for y in self.operand1.eno()] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound) for y in self.operand2.eno()]

    @remove_duplicates
    def rro(self):
        return [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.rro() if not y == self.operand2] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.rro() if not y == self.operand1]

    @remove_duplicates
    def mco(self):
        return [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound) for y in self.operand1.mco()] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound) for y in self.operand2.mco()]

    @remove_duplicates
    def sto(self, onezero):
        return [RELEASE(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.sto(onezero) if not y == self.operand2] \
               + [RELEASE(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.sto(onezero) if not y == self.operand1]

    def ufc_plus(self):
        from _not import NOT
        from until import UNTIL
        return NOT(UNTIL(NOT(self.operand1), NOT(self.operand2), self.lower_bound, self.upper_bound)).ufc_plus()

    def ufc_minus(self):
        from _not import NOT
        from until import UNTIL
        return NOT(UNTIL(NOT(self.operand1), NOT(self.operand2), self.lower_bound, self.upper_bound)).ufc_minus()

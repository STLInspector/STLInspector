from clause import *


class NEXT(Clause):
    """
    This class represents the temporal logic operation 'next'.
    
    The class can be used for both STL and LTL Next-operators.
    When it is used for LTL the interval bound is simply set to None.
    
    Attributes:
        operand (Clause) : Operand of this unary temporal logic expression.
        bound (int) : Boundary for STL Nexts.

    Clause attributes that are set: namestring (str) : String "N" used for printing.
        
    Examples:
        NEXT(AP("a")) - N (a)
        NEXT(FINALLY(AP("a"), 1, 2), 3) - N[3](F[1,2](a))
        NEXT(AND(AP("a"), OR(AP("b"), NEXT(AP("c")))) - N(a & (b | N(c)))
    """
    
    def __init__(self, operand, bound=None):
        Clause.__init__(self, "N", operand, None, bound)
    
    # Overwrites method of class Clause
    def expand(self):
        return NEXT(self.operand1.expand(), self.lower_bound)
    
    # Overwrites method of class Clause
    def negationnormalform(self):
        return NEXT(self.operand1.negationnormalform(), self.lower_bound)
    
    # Overwrites method of class Clause
    def nextnormalform(self, ininterval=0):
        return NEXT(self.operand1.nextnormalform(ininterval), self.lower_bound)
            
    # Overwrites method of class Clause            
    def encode(self, state=0):
        state += 1 if self.lower_bound is None else self.lower_bound
        return self.operand1.encode(state)
    
    # Overwrites method of class Clause    
    def get_aps(self):
        return self.operand1.get_aps()

    def length(self):
        """ Calculates the length (number of time steps) of a given formula. """
        return self.operand1.length() + self.lower_bound

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        return NEXT(self.operand1.adjust(c), self.lower_bound / float(c))

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        return self.operand1.getLimits() + [self.lower_bound]

    @remove_duplicates
    def aso(self):
        return [NEXT(y, self.lower_bound) for y in self.operand1.aso()]

    @remove_duplicates
    def mto(self):
        return [self.operand1] + [NEXT(y, self.lower_bound) for y in self.operand1.mto()]

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        return [NEXT(y, self.lower_bound) for y in self.operand1.tio(lower_bound, upper_bound)]

    @remove_duplicates
    def ano(self):
        return [NEXT(y, self.lower_bound) for y in self.operand1.ano()]

    @remove_duplicates
    def oro(self, atomic_props):
        return [NEXT(y, self.lower_bound) for y in self.operand1.oro(atomic_props)]

    @remove_duplicates
    def lro(self):
        return [NEXT(y, self.lower_bound) for y in self.operand1.lro()]

    @remove_duplicates
    def tro(self):
        from _finally import FINALLY
        from globally import GLOBALLY
        return [FINALLY(self.operand1, self.lower_bound, self.lower_bound),
                GLOBALLY(self.operand1, self.lower_bound, self.lower_bound)] \
               + [NEXT(y, self.lower_bound) for y in self.operand1.tro()]

    @remove_duplicates
    def io(self):
        return [NEXT(self.operand1, self.lower_bound + 1)] \
               + [NEXT(self.operand1, self.lower_bound - 1) for fake_iterator in [1] if not self.lower_bound == 0] \
               + [NEXT(y, self.lower_bound) for y in self.operand1.io()]

    @remove_duplicates
    def eno(self):
        return [NEXT(y, self.lower_bound) for y in self.operand1.eno()]

    @remove_duplicates
    def rro(self):
        return [NEXT(y, self.lower_bound) for y in self.operand1.rro()]

    @remove_duplicates
    def mco(self):
        return [NEXT(y, self.lower_bound) for y in self.operand1.mco()]

    @remove_duplicates
    def sto(self, onezero):
        return [NEXT(y, self.lower_bound) for y in self.operand1.sto(onezero)]

    def ufc_plus(self):
        return [NEXT(y, self.lower_bound) for y in self.operand1.ufc_plus()]

    def ufc_minus(self):
        return [NEXT(y, self.lower_bound) for y in self.operand1.ufc_minus()]


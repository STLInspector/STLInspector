from clause import *


class FINALLY(Clause):
    """
    This class represents the temporal logic operation 'finally'.
    
    The class can be used for both STL and LTL Finally-operators.
    When it is used for LTL the interval bounds are simply set to None.
    
    Attributes:
        operand (Clause) : Operand of this unary temporal logic expression.
        lower_bound (int) : Lower boundary for STL interval.
        upper_bound (int) : Upper boundary for STL interval.

    Clause attributes that are set: namestring (str) : String "F" used for printing.
        
    Examples:
        FINALLY(AP("a")) - F (a)
        FINALLY(NEXT(AP("a"), 1, 2), 3, 4) - F[3,4](N[1,2](a))
        FINALLY(AND(AP("a"), OR(AP("b"), FINALLY(AP("c"))))) - F(a & (b | F(c)))
    """
    
    def __init__(self, operand, lower_bound=None, upper_bound=None):
        Clause.__init__(self, "F", operand, None, lower_bound, upper_bound)
    
    # Overwrites method of class Clause        
    def expand(self):
        from until import UNTIL
        from ap import ap_true
        return UNTIL(ap_true, self.operand1.expand(), self.lower_bound, self.upper_bound)
    
    # Overwrites method of class Clause
    # Does not need a negationnormalform since its rewritten as Until beforehand
    def negationnormalform(self):
        pass
    
    # Overwrites method of class Clause      
    # Does not need a nextnormalform function since its rewritten as Until beforehand
    def nextnormalform(self, ininterval=0):
        pass
    
    # Overwrites method of class Clause      
    # Does not need an encoding function since its rewritten as Until beforehand
    def encode(self, state=0):
        pass
    
    # Overwrites method of class Clause    
    def get_aps(self):
        return self.operand1.get_aps()

    def length(self):
        """ Calculates the range (number of time steps) of a given formula. """
        return self.operand1.length() + self.upper_bound

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        return FINALLY(self.operand1.adjust(c), self.lower_bound / float(c), self.upper_bound / float(c))

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        return self.operand1.getLimits() + [self.lower_bound, self.upper_bound]

    @remove_duplicates
    def aso(self):
        return [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.aso()]
        
    @remove_duplicates
    def mto(self):
        return [self.operand1] + [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.mto()]

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        return [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.tio(lower_bound, upper_bound)]

    @remove_duplicates
    def ano(self):
        return [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.ano()]

    @remove_duplicates
    def oro(self, atomic_props):
        return [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.oro(atomic_props)]

    @remove_duplicates
    def lro(self):
        return [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.lro()]

    @remove_duplicates
    def tro(self):
        from next import NEXT
        from globally import GLOBALLY
        return [NEXT(self.operand1, self.upper_bound), GLOBALLY(self.operand1, self.lower_bound, self.upper_bound)] \
               + [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.tro()]

    @remove_duplicates
    def io(self):
        return [FINALLY(self.operand1, self.lower_bound + 1, self.upper_bound)] \
               + [FINALLY(self.operand1, self.lower_bound - 1, self.upper_bound)
                  for fake_iterator in [1] if not self.lower_bound == 0] \
               + [FINALLY(self.operand1, self.lower_bound, self.upper_bound + 1)] \
               + [FINALLY(self.operand1, self.lower_bound, self.upper_bound - 1)] \
               + [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.io()]

    @remove_duplicates
    def eno(self):
        return [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.eno()]

    @remove_duplicates
    def rro(self):
        return [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.rro()]

    @remove_duplicates
    def mco(self):
        return [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.mco()]

    @remove_duplicates
    def sto(self, onezero):
        return [FINALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.sto(onezero)]

    def ufc_plus(self):
        from until import UNTIL
        from _not import NOT
        return [UNTIL(NOT(self.operand1), y, self.lower_bound, self.upper_bound) for y in self.operand1.ufc_plus()]

    def ufc_minus(self):
        from until import UNTIL
        from _not import NOT
        from _and import AND
        from globally import GLOBALLY
        return [UNTIL(NOT(self.operand1),
                      AND(y, GLOBALLY(NOT(self.operand1), self.lower_bound, self.upper_bound)), 
                      self.lower_bound, self.upper_bound) for y in self.operand1.ufc_minus()]
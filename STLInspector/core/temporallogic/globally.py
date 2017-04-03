from clause import *


class GLOBALLY(Clause):
    """
    This class represents the temporal logic operation 'globally'.

    The class can be used for both STL and LTL Globally-operators.
    When it is used for LTL the interval bounds are simply set to None.

    Attributes:
        operand (Clause) : Operand of this unary temporal logic expression.
        lower_bound (int) : Lower boundary for STL interval.
        upper_bound (int) : Upper boundary for STL interval.

    Clause attributes that are set: namestring (str) : String "G" used for printing.

    Examples:
        GLOBALLY(AP("a")) - G (a)
        GLOBALLY(FINALLY(AP("a"), 1, 2), 3, 4) - G[3,4](F[1,2](a))
        GLOBALLY(AND(AP("a"), OR(AP("b"), GLOBALLY(AP("c"))))) - G(a & (b | G(c)))
    """

    def __init__(self, operand, lower_bound=None, upper_bound=None):
        Clause.__init__(self, "G", operand, None, lower_bound, upper_bound)

    # Overwrites method of class Clause
    def expand(self):
        from _not import NOT
        from until import UNTIL
        from ap import ap_true
        return NOT(UNTIL(ap_true, NOT(self.operand1.expand()), self.lower_bound, self.upper_bound))

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
        """ Calculates the length (number of time steps) of a given formula. """
        return self.operand1.length() + self.upper_bound

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        return GLOBALLY(self.operand1.adjust(c), self.lower_bound / float(c), self.upper_bound / float(c))

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        return self.operand1.getLimits() + [self.lower_bound, self.upper_bound]

    @remove_duplicates
    def aso(self):
        return [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.aso()]

    @remove_duplicates
    def mto(self):
        return [self.operand1] + [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.mto()]

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        return [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.tio(lower_bound, upper_bound)]

    @remove_duplicates
    def ano(self):
        return [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.ano()]

    @remove_duplicates
    def oro(self, atomic_props):
        return [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.oro(atomic_props)]

    @remove_duplicates
    def lro(self):
        return [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.lro()]

    @remove_duplicates
    def tro(self):
        from next import NEXT
        from _finally import FINALLY
        return [NEXT(self.operand1, self.upper_bound), FINALLY(self.operand1, self.lower_bound, self.upper_bound)] \
               + [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.tro()]

    @remove_duplicates
    def io(self):
        return [GLOBALLY(self.operand1, self.lower_bound + 1, self.upper_bound)] \
               + [GLOBALLY(self.operand1, self.lower_bound - 1, self.upper_bound)
                  for fake_iterator in [1] if not self.lower_bound == 0] \
               + [GLOBALLY(self.operand1, self.lower_bound, self.upper_bound + 1)] \
               + [GLOBALLY(self.operand1, self.lower_bound, self.upper_bound - 1)] \
               + [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.io()]

    @remove_duplicates
    def eno(self):
        return [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.eno()]

    @remove_duplicates
    def rro(self):
        return [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.rro()]

    @remove_duplicates
    def mco(self):
        return [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.mco()]

    @remove_duplicates
    def sto(self, onezero):
        return [GLOBALLY(y, self.lower_bound, self.upper_bound) for y in self.operand1.sto(onezero)]

    def ufc_plus(self):
        from until import UNTIL
        from _and import AND
        return [UNTIL(self.operand1, 
                      AND(y, GLOBALLY(self.operand1, self.lower_bound, self.upper_bound)), 
                      self.lower_bound, self.upper_bound) for y in self.operand1.ufc_plus()]

    def ufc_minus(self):
        from until import UNTIL
        return [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound) for y in self.operand1.ufc_minus()]


from clause import *


class UNTIL(Clause):
    """
    This class represents the temporal logic operation 'until'.

    The class can be used for both STL and LTL Until-operators.
    When it is used for LTL the interval bounds are simply set to None.

    Attributes:
        operand1 (Clause) : First operand of this binary temporal logic expression.
        operand2 (Clause) : Second operand of this binary temporal logic expression.
        lower_bound (int) : Lower boundary for STL interval.
        upper_bound (int) : Upper boundary for STL interval.

    Clause attributes that are set: namestring (str) : String "U" used for printing.

    Examples:
        UNTIL(AP("a"), AP("b")) - a U b
        UNTIL(AP("a"), FINALLY(AP("b"), 1, 2), 3, 4) - a U[3,4] (F[1,2] b)
        UNTIL(AP("a"), OR(AP("b"), UNTIL(AP("c"), AP("d")))) - a U (b | (c U d))
    """

    def __init__(self, operand1, operand2, lower_bound=None, upper_bound=None):
        Clause.__init__(self, "U", operand1, operand2, lower_bound, upper_bound)

    # Overwrites method of class Clause
    def expand(self):
        return UNTIL(self.operand1.expand(), self.operand2.expand(), self.lower_bound, self.upper_bound)

    # Overwrites method of class Clause
    # Does not need a negationnormalform since its rewritten as Nexts beforehand
    def negationnormalform(self):
        pass

    # Overwrites method of class Clause
    def nextnormalform(self, ininterval=0):
        from _or import OR
        from _and import AND
        from next import NEXT
        if self.lower_bound == 0 and self.upper_bound == 0:
            return self.operand2.nextnormalform(ininterval)
        elif (self.lower_bound == 0 and (not self.upper_bound == 0)
              and ininterval % 2 == 0):
            return OR(self.operand2.nextnormalform(ininterval), AND(self.operand1.nextnormalform(ininterval), AND(
                NEXT(self.operand1.nextnormalform(ininterval + 1), 0.5),
                OR(NEXT(self.operand2.nextnormalform(ininterval + 1), 0.5),
                   NEXT(UNTIL(self.operand1, self.operand2, 0, self.upper_bound - 1).nextnormalform(ininterval), 1)))))
        elif (self.lower_bound == 0 and (not self.upper_bound == 0)
              and ininterval % 2 == 1):
            return OR(self.operand2.nextnormalform(ininterval), AND(self.operand1.nextnormalform(ininterval), OR(
                NEXT(self.operand2.nextnormalform(ininterval + 1), 0.5),
                AND(NEXT(self.operand1.nextnormalform(ininterval + 1), 0.5),
                    AND(NEXT(self.operand1.nextnormalform(ininterval), 1),
                        NEXT(UNTIL(self.operand1, self.operand2, 0, self.upper_bound - 1).nextnormalform(ininterval),
                             1))))))
        elif ((not self.lower_bound == 0) and (not self.upper_bound == 0)
              and ininterval % 2 == 0):
            return AND(self.operand1.nextnormalform(ininterval),
                       AND(NEXT(self.operand1.nextnormalform(ininterval + 1), 0.5), NEXT(
                           UNTIL(self.operand1, self.operand2, self.lower_bound - 1,
                                 self.upper_bound - 1).nextnormalform(ininterval), 1)))
        elif ((not self.lower_bound == 0) and (not self.upper_bound == 0)
              and ininterval % 2 == 1):
            return AND(self.operand1.nextnormalform(ininterval),
                       AND(NEXT(self.operand1.nextnormalform(ininterval + 1), 0.5),
                           AND(NEXT(self.operand1.nextnormalform(ininterval), 1), NEXT(
                               UNTIL(self.operand1, self.operand2, self.lower_bound - 1,
                                     self.upper_bound - 1).nextnormalform(ininterval), 1))))

    # Overwrites method of class Clause
    # Does not need an encoding function since its rewritten as Next beforehand
    def encode(self, state=0):
        pass

    def length(self):
        """ Calculates the length (number of time steps) of a given formula. """
        return max(self.operand1.length(), self.operand2.length()) + self.upper_bound

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        return UNTIL(self.operand1.adjust(c), self.operand2.adjust(c),
                     self.lower_bound / float(c), self.upper_bound / float(c))

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        return self.operand1.getLimits() + self.operand2.getLimits() + [self.lower_bound, self.upper_bound]

    @remove_duplicates
    def aso(self):
        from release import RELEASE
        from _and import AND
        from _or import OR
        from implies import IMPLIES
        from _finally import FINALLY
        from globally import GLOBALLY
        from next import NEXT
        result = list()
        if isinstance(self.operand1, (UNTIL, RELEASE)):
            result += [self.operand1.__class__(self.operand1.operand1,
                                               UNTIL(self.operand1.operand2, self.operand2, self.lower_bound,
                                                     self.upper_bound),
                                               self.operand1.lower_bound, self.operand1.upper_bound)]
        if isinstance(self.operand2, (UNTIL, RELEASE)):
            result += [self.operand2.__class__(UNTIL(self.operand1, self.operand2.operand1,
                                                     self.lower_bound, self.upper_bound),
                                               self.operand2.operand2, self.operand2.lower_bound,
                                               self.operand2.upper_bound)]
        if isinstance(self.operand1, (AND, OR, IMPLIES)):
            result += [self.operand1.__class__(self.operand1.operand1,
                                               UNTIL(self.operand1.operand2, self.operand2,
                                                     self.lower_bound, self.upper_bound))]
        if isinstance(self.operand2, (AND, OR, IMPLIES)):
            result += [self.operand2.__class__(UNTIL(self.operand1, self.operand2.operand1,
                                                     self.lower_bound, self.upper_bound), self.operand2.operand2)]
        if isinstance(self.operand1, (FINALLY, GLOBALLY)):
            result += [self.operand1.__class__(UNTIL(self.operand1.operand1, self.operand2,
                                                     self.lower_bound, self.upper_bound),
                                               self.operand1.lower_bound, self.operand1.upper_bound)]
        if isinstance(self.operand2, (FINALLY, GLOBALLY)):
            result += [self.operand2.__class__(UNTIL(self.operand1, self.operand2.operand1,
                                                     self.lower_bound, self.upper_bound),
                                               self.operand2.lower_bound, self.operand2.upper_bound)]
        if isinstance(self.operand1, NEXT):
            result += [NEXT(UNTIL(self.operand1.operand1, self.operand2, self.lower_bound, self.upper_bound),
                            self.operand1.lower_bound)]
        if isinstance(self.operand2, NEXT):
            result += [NEXT(UNTIL(self.operand1, self.operand2.operand1, self.lower_bound, self.upper_bound),
                            self.operand2.lower_bound)]
        return result + [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound)
                         for y in self.operand1.aso() if not y == self.operand2] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.aso() if not y == self.operand1]

    @remove_duplicates
    def mto(self):
        return [self.operand1, self.operand2] \
               + [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound) for y in self.operand1.mto()] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound) for y in self.operand2.mto()]

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        return [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.tio(lower_bound, upper_bound) if not y == self.operand2] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.tio(lower_bound, upper_bound) if not y == self.operand1]

    @remove_duplicates
    def ano(self):
        return [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.ano() if not y == self.operand2] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.ano() if not y == self.operand1]

    @remove_duplicates
    def oro(self, atomic_props):
        return [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.oro(atomic_props) if not y == self.operand2] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.oro(atomic_props) if not y == self.operand1]

    @remove_duplicates
    def lro(self):
        return [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.lro() if not y == self.operand2] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.lro() if not y == self.operand1]

    @remove_duplicates
    def tro(self):
        from release import RELEASE
        return [RELEASE(self.operand1, self.operand2, self.lower_bound, self.upper_bound)] \
               + [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound)
                  for y in self.operand1.tro() if not y == self.operand2] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.tro() if not y == self.operand1]

    @remove_duplicates
    def io(self):
        return [UNTIL(self.operand1, self.operand2, self.lower_bound + 1, self.upper_bound),
                UNTIL(self.operand1, self.operand2, self.lower_bound, self.upper_bound + 1),
                UNTIL(self.operand1, self.operand2, self.lower_bound, self.upper_bound - 1)] \
               + [UNTIL(self.operand1, self.operand2, self.lower_bound - 1, self.upper_bound)
                  for fake_iterator in [1] if not self.lower_bound == 0] \
               + [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound) for y in self.operand1.io()] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound) for y in self.operand2.io()]

    @remove_duplicates
    def eno(self):
        return [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound) for y in self.operand1.eno()] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound) for y in self.operand2.eno()]

    @remove_duplicates
    def rro(self):
        return [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.rro() if not y == self.operand2] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.rro() if not y == self.operand1]

    @remove_duplicates
    def mco(self):
        return [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound) for y in self.operand1.mco()] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound) for y in self.operand2.mco()]

    @remove_duplicates
    def sto(self, onezero):
        return [UNTIL(y, self.operand2, self.lower_bound, self.upper_bound)
                for y in self.operand1.sto(onezero) if not y == self.operand2] \
               + [UNTIL(self.operand1, y, self.lower_bound, self.upper_bound)
                  for y in self.operand2.sto(onezero) if not y == self.operand1]

    def ufc_plus(self):
        from until import UNTIL
        from _and import AND
        from _not import NOT
        return [UNTIL(AND(self.operand1, NOT(self.operand2)), 
                      AND(AND(y, NOT(self.operand2)),
                          UNTIL(self.operand1, self.operand2, self.lower_bound, self.upper_bound)),
                      self.lower_bound, self.upper_bound) for y in self.operand1.ufc_plus()] \
               + [UNTIL(AND(self.operand1, NOT(self.operand2)), y, self.lower_bound, self.upper_bound) 
                  for y in self.operand2.ufc_plus()]

    def ufc_minus(self):
        from until import UNTIL
        from _and import AND
        from _not import NOT
        return [UNTIL(AND(self.operand1, NOT(self.operand2)), 
                      AND(y, NOT(self.operand2)), self.lower_bound, self.upper_bound)
                for y in self.operand1.ufc_minus()] \
               + [UNTIL(AND(self.operand1, NOT(self.operand2)), 
                        AND(y, NOT(UNTIL(self.operand1, self.operand2, self.lower_bound, self.upper_bound))), 
                        self.lower_bound, self.upper_bound) for y in self.operand2.ufc_minus()]

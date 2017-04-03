from clause import *


class NOT(Clause):
    """
    This class represents the logical operation 'not'.
    
    Attributes:
        operand (Clause) : Operand of this unary logical expression.

    Clause attributes that are set: namestring (str) : String "!" used for printing.
        
    Examples:
        NOT(AP("a")) - !a
        NOT(AND(AP("a"), OR(AP("b"), NOT(AP("c")))) - !(a & (b | (!c)))
    """
    
    def __init__(self, operand):
        Clause.__init__(self, "!", operand)
    
    # Overwrites method of class Clause
    def expand(self):
        return NOT(self.operand1.expand())
    
    # Overwrites method of class Clause
    def nextnormalform(self, ininterval=0):
        return NOT(self.operand1.nextnormalform(ininterval))
    
    # Overwrites methods of class Clause
    # Uses De Morgan's laws and removes double negation
    def negationnormalform(self):
        from ap import ap_true, ap_false, AP
        from _or import OR
        from _and import AND
        from implies import IMPLIES
        from next import NEXT
        if isinstance(self.operand1, AP):
            if self.operand1 == ap_true:
                return ap_false
            elif self.operand1 == ap_false:
                return ap_true
            elif self.operand1.operator is None:  # Boolean AP
                return self
            elif self.operand1.operator == ge:
                return AP(None, self.operand1.c, lt, self.operand1.b, self.operand1.variables)
            elif self.operand1.operator == gt:
                return AP(None, self.operand1.c, le, self.operand1.b, self.operand1.variables)
            elif self.operand1.operator == le:
                return AP(None, self.operand1.c, gt, self.operand1.b, self.operand1.variables)
            elif self.operand1.operator == lt:
                return AP(None, self.operand1.c, ge, self.operand1.b, self.operand1.variables)
            elif self.operand1.operator == eq:
                return AP(None, self.operand1.c, ne, self.operand1.b, self.operand1.variables)
            elif self.operand1.operator == ne:
                return AP(None, self.operand1.c, eq, self.operand1.b, self.operand1.variables)
        elif isinstance(self.operand1, AND):
            return OR(NOT(self.operand1.operand1).negationnormalform(),
                      NOT(self.operand1.operand2).negationnormalform())
        elif isinstance(self.operand1, OR):
            return AND(NOT(self.operand1.operand1).negationnormalform(),
                       NOT(self.operand1.operand2).negationnormalform())
        elif isinstance(self.operand1, IMPLIES):
            return NOT(self.operand1.negationnormalform()).negationnormalform()
        elif isinstance(self.operand1, NOT):
            return self.operand1.operand1.negationnormalform()
        elif isinstance(self.operand1, NEXT):
            return NEXT(NOT(self.operand1.operand1).negationnormalform(), self.operand1.lower_bound)
        # Other type of operands do not exist since negationnormalform is called after nextnormalform
        
    # Overwrite method of class Clause
    def encode(self, state=0):
        operand_enc = self.operand1.encode(state)
        return "(not {0})".format(operand_enc[0]), operand_enc[1]
    
    # Overwrites method of class Clause    
    def get_aps(self):
        return self.operand1.get_aps()

    def __len__(self):
        """ Calculates the range (number of time steps) of a given formula. """
        return self.operand1.__len__()

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        return NOT(self.operand1.adjust(c))

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        return self.operand1.getLimits()

    @remove_duplicates
    def aso(self):
        return [NOT(y) for y in self.operand1.aso()]

    @remove_duplicates
    def mto(self):
        return [NOT(y) for y in self.operand1.mto()]

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        from _finally import FINALLY
        from globally import GLOBALLY
        from next import NEXT
        return [NOT(FINALLY(self.operand1, lower_bound, upper_bound)),
                NOT(GLOBALLY(self.operand1, lower_bound, upper_bound)),
                NOT(NEXT(self.operand1, upper_bound))] \
               + [NOT(y) for y in self.operand1.tio(lower_bound, upper_bound)]

    @remove_duplicates
    def ano(self):
        return [NOT(y) for y in self.operand1.ano()]

    @remove_duplicates
    def oro(self, atomic_props):
        return [NOT(y) for y in self.operand1.oro(atomic_props)]

    @remove_duplicates
    def lro(self):
        return [NOT(y) for y in self.operand1.lro()]

    @remove_duplicates
    def tro(self):
        return [NOT(y) for y in self.operand1.tro()]

    @remove_duplicates
    def io(self):
        return [NOT(y) for y in self.operand1.io()]

    @remove_duplicates
    def eno(self):
        return [y for y in self.operand1.eno()]

    @remove_duplicates
    def rro(self):
        return [NOT(y) for y in self.operand1.rro()]

    @remove_duplicates
    def mco(self):
        return [NOT(y) for y in self.operand1.mco()]

    @remove_duplicates
    def sto(self, onezero):
        return [NOT(y) for y in self.operand1.sto(onezero)]

    def ufc_plus(self):
        return [y for y in self.operand1.ufc_minus()]

    def ufc_minus(self):
        return [y for y in self.operand1.ufc_plus()]

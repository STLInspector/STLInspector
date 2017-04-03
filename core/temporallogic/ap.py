from clause import *


class AP(Clause):
    """
    This class represents an atomic proposition.
    
    Atomic propositions can be either in Boolean or in real format.
    The Boolean format consists of simply one variable. The real
    format is of the form c^T * x <relational operator> b. In this
    format the attribute c is optional.
    
    Attributes:
        name (str) : String used for printing.
        c (tuple) : Tuple of integers.
        operator (operator) : Can be one of the following
                              operator.lt(a, b) -- <
                              operator.le(a, b) -- <=
                              operator.eq(a, b) -- ==
                              operator.ne(a, b) -- !=
                              operator.ge(a, b) -- >=
                              operator.gt(a, b) -- >
        b (float) : Boundary value.
        variables (tuple) : Tuple of string that represent
                            variables. The tuple has the
                            same length as the attribute c.
                            
    Examples:
        AP("engine_is_on") - Boolean atomic proposition.
        AP(None, (1,2), operator.ge, 3, ('a', 'b')) - Real atomic proposition 1a+2b >= 3.
        AP(None, (3,) , operator.ne, 4, 'a') - Real atomic proposition 3a != 4.
        AP(None, None , operator.lt, 42, 'a') - Real atomic proposition a < 42.        
    """
    
    def __init__(self, name, c=None, operator=None, b=None, variables=None):
        self.c = None if c is None else [float(x) for x in c if (isinstance(x, (float, int)) or x.replace('.', '').replace(' ', '').lstrip('-+').isdigit())]
        self.operator = operator
        self.b = b
        self.variables = None if variables is None else [str(x.strip()) for x in variables if not x == '']
        self.name = self.get_name(name)
        
    def get_name(self, name):     
        if name is not None:
            return name
        else:
            o = {
                gt: '>',
                lt: '<',
                ge: '>=',
                le: '<=',
                eq: '==',
                ne: "!="
            }
            if self.c is not None and not self.c == list():
                if len(self.c) == 1:
                    return '{0} {1} {2} {3}'.format(self.c[0], self.variables[0], o[self.operator], self.b)
                return '{0}^T {1} {2} {3}'.format(tuple(self.c), tuple(self.variables), o[self.operator], self.b)
            elif self.b is not None:
                if len(self.variables) == 1:
                    return '{0} {1} {2}'.format(self.variables[0], o[self.operator], self.b)
                return '{0} {1} {2}'.format(tuple(self.variables), o[self.operator], self.b)
        
    def __str__(self):         
        return str(self.name).translate(None, "'")
    
    def __eq__(self, other):
        return (isinstance(other, AP) and other.name == self.name and other.c == self.c
                and other.operator == self.operator and other.b == self.b and other.variables == self.variables)
    
    def expand(self):
        return self
    
    def negationnormalform(self):
        return self
    
    def nextnormalform(self, ininterval=0):
        return self
    
    def encode(self, state=0):
        
        def single_encode(ap, s):
            o = {
                    gt: '>',
                    lt: '<',
                    ge: '>=',
                    le: '<=',
                    eq: '=',
                    ne: "distinct"
                }
        
            def add_variables(l1, l2=[]):
                if len(l1) == 1:
                    if len(l2) == 0:
                        return '{0}'.format(l1[0])
                    else:
                        return '(* {0} {1})'.format(l1[0], l2[0])
                else:
                    return '(+ {0} {1})'.format(add_variables(l1[:1], l2[:1]), 
                                                add_variables(l1[1:], l2[1:]))
            
            # Logical format was used for atomic propositions
            if ap.c is None and ap.operator is None and ap.b is None:
                boolean = '{0}___{1}'.format(ap.name, float(s))
                declaration = '(declare-const {0} Bool)'.format(boolean)
                return boolean, [declaration]
            # Real format without c (f.ex. x < b) was used for atomic propositions
            elif ap.c == [] or ap.c is None:
                reals = ["{0}___{1}".format(z, float(s)) for z in ap.variables]
                declarations = ['(declare-const {0} Real)'.format(z) for z in reals]
                return '({0} {1} {2})'.format(o[ap.operator], add_variables(reals),  ap.b), declarations
            else:
                # Real format (f.ex. c^T * x < b) was used for atomic propositions
                reals = ["{0}___{1}".format(z, float(s)) for z in ap.variables]
                declarations = ['(declare-const {0} Real)'.format(z) for z in reals]
                return '({0} {1} {2})'.format(o[ap.operator], add_variables(ap.c, reals),  ap.b), declarations
        
        if (self.operator is not None) and (2 * state) % 2 == 1:
            # Append APs at interval bounds to ensure continuity
            if self.operator == gt:
                bound_ap = AP(None, self.c, ge, self.b, self.variables)
            elif self.operator == lt:
                bound_ap = AP(None, self.c, le, self.b, self.variables)
            elif self.operator == ne:
                left = single_encode(AP(None, self.c, lt, self.b, self.variables), state-0.5)
                right = single_encode(AP(None, self.c, gt, self.b, self.variables), state+0.5)
                self_enc = single_encode(self, state)
                return '(and {0} (and {1} {2}))'.format(left[0], self_enc[0], right[0]), \
                       list(set(left[1] + self_enc[1] + right[1]))
            else:
                bound_ap = self
            left = single_encode(bound_ap, state-0.5)
            right = single_encode(bound_ap, state+0.5)
            self_enc = single_encode(self, state)
            return '(and {0} (and {1} {2}))'.format(left[0], self_enc[0], right[0]), \
                   list(set(left[1] + self_enc[1] + right[1]))
        else:
            return single_encode(self, state)

    def get_aps(self):
        return [self]
    
    def __hash__(self):
        return hash(self.name)

    def length(self):
        """ Calculates the length (number of time steps) of a given formula. """
        return 0

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        return self

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        return []

    @remove_duplicates
    def aso(self):
        return [self]

    @remove_duplicates
    def mto(self):
        return[self]

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        from _finally import FINALLY
        from globally import GLOBALLY
        from next import NEXT
        return [FINALLY(self, lower_bound, upper_bound),
                GLOBALLY(self, lower_bound, upper_bound),
                NEXT(self, upper_bound), self]

    @remove_duplicates
    def ano(self):
        from _not import NOT
        return [NOT(self)]

    @remove_duplicates
    def oro(self, atomic_props):
        return [y for y in atomic_props if not y == self]

    @remove_duplicates
    def lro(self):
        return [self]

    @remove_duplicates
    def tro(self):
        return [self]

    @remove_duplicates
    def io(self):
        return [self]

    @remove_duplicates
    def eno(self):
        return [self]

    @remove_duplicates
    def rro(self):
        if self.operator is not None:
            operators = {lt, le, gt, ge, eq, ne}
            opposite = {
                lt: [ge],
                ge: [lt],
                le: [gt],
                gt: [le],
                eq: [ne],
                ne: [eq]
            }
            return [AP(None, self.c, o, self.b, self.variables) for o in operators if
                (o not in opposite[self.operator] and not o == self.operator)]
        else:
            return [self]

    @remove_duplicates
    def mco(self):
        return [self]

    @remove_duplicates
    def sto(self, onezero):
        return [ap_true] if (onezero == 1) else [ap_false]

    def ufc_plus(self):
        return [self]

    def ufc_minus(self):
        from _not import NOT
        return [NOT(self)]


# True and False are defined during the whole program
ap_true = AP("True")
ap_true.encode = lambda x: ("true", [])
ap_true.negationnormalform = lambda: ap_true
ap_false = AP("False")
ap_false.encode = lambda x: ("false", [])
ap_false.negationnormalform = lambda: ap_false

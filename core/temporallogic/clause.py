from operator import *


# Define decorator/wrapper for mutation operators to filter out duplicate mutants
def remove_duplicates(func):
    def rm_dub(*args, **kwargs):
        res = list()
        result = func(*args, **kwargs)
        if result is not None:
            for x in result:
                if x not in res:
                    res.append(x)
        return res
    return rm_dub


class Clause:
    """ This class is the parent class of all other ((signal) temporal) logic classes."""
    
    def __init__(self, namestring, operand1=None, operand2=None, lower_bound=None, upper_bound=None):
        self.namestring = namestring
        self.operand1 = operand1
        self.operand2 = operand2
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        
    def __str__(self):
        # Unary logical connective or unary LTL connective
        if self.operand2 is None and self.lower_bound is None and self.upper_bound is None:
            return '({0} {1})'.format(self.namestring, self.operand1)
        # Binary logical connective or binary LTL connective
        elif self.lower_bound is None and self.upper_bound is None:
            return '({0} {1} {2})'.format(self.operand1, self.namestring, self.operand2)
        # STL Next
        elif self.operand2 is None and self.upper_bound is None:
            return '({0}[{1}] {2})'.format(self.namestring, self.lower_bound, self.operand1)
        # Unary STL connective
        elif self.operand2 is None:
            return '({0}[{1},{2}] {3})'.format(self.namestring, self.lower_bound, self.upper_bound, self.operand1)
        # Binary STL connective
        else:
            return '({0} {1}[{2},{3}] {4})'.format(self.operand1, self.namestring,
                                                   self.lower_bound, self.upper_bound, self.operand2)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__) \
                and other.operand1 == self.operand1 \
                and other.operand2 == self.operand2 \
                and other.lower_bound == self.lower_bound \
                and other.upper_bound == self.upper_bound:
            return True
        else:
            return False
    
    # Only valid for AND, OR and IMPLIES - all other classes overwrite this method
    def expand(self):
        return self.__class__(self.operand1.expand(), self.operand2.expand())
    
    # Only valid for AND and OR - all other classes overwrite this method
    def negationnormalform(self):
        return self.__class__(self.operand1.negationnormalform(), self.operand2.negationnormalform())
    
    # Only valid for AND, OR and IMPLIES - all other classes overwrite this method
    def nextnormalform(self, ininterval=0):
        return self.__class__(self.operand1.nextnormalform(ininterval), self.operand2.nextnormalform(ininterval))
    
    # Only valid for AND, OR and IMPLIES - all other classes overwrite this method
    def encode(self, state=0):
        firstoperand = self.operand1.encode(state)
        secondoperand = self.operand2.encode(state)
        return "({0} {1} {2})".format(self.__class__.__name__.lower(), firstoperand[0], secondoperand[0]), \
               firstoperand[1]+secondoperand[1]
    
    # Only valid for binary connectives - all other classes overwrite this method
    def get_aps(self):
        return self.operand1.get_aps() + self.operand2.get_aps()
    
    def __hash__(self):
        return hash(self.namestring) ^ hash(self.operand1)

    def length(self):
        """ Calculates the length (number of time steps) of a given formula. """
        pass

    def adjust(self, c):
        """ Adjusts formula to a given step width c by dividing all interval bounds by c. """
        pass

    def getLimits(self):
        """ Returns list of integers used as interval limits. """
        pass

    @remove_duplicates
    def aso(self):
        """ Generate mutants for the associate shift operator [0].

        For every nested (temporal) logical expression with two operators
        in a given formula one mutated formula is created that holds the
        same expression but with different associativity of the two operators.

        Examples:
            a & (b | c) is mutated into (a & b) | c
            a U (b R c) is mutated into (a U b) R c
            (F a) U b is mutated into F(a U b)

        Args:
            self (Clause) : The formula for which mutants are generated.

        Returns:
            list: Temporal logic formulae that are mutants for the
            associate shift operator of the given formula x.

        References:
            [0] : Black, P.E., Okun, V., Yesha, Y.: Mutation Operators for
            Specifications. In: Proceedings of the Fifteenth IEEE International
            Conference on Automated Software Engineering (ASE 2000), Washington,
            DC, USA. IEEE Computer Society Press, Los Alamitos (2000).
        """
        pass

    @remove_duplicates
    def mto(self):
        """ Generate mutants for the missing temporal operator [0].

        For each temporal expression in a given formula one mutant is
        created that holds the operant of the temporal expression
        in the same place but without the temporal operator.

        Examples:
            a & (F b) is mutated into a & b
            a U b is mutated into the two formulae a and b

        Args:
            self (Clause) : The formula for which mutants are generated.

        Returns:
            list: Temporal logic formulae that are mutants for the
            missing temporal operator of the given formula x.

        References:
            [0] : Gordon Fraser and Franz Wotawa, Complementary Criteria for Testing
            Temporal Logic Properties, TAP '09 Proceedings of the 3rd International
            Conference on Tests and Proofs, Pages 58 - 73, 2009.
        """
        pass

    @remove_duplicates
    def tio(self, lower_bound=None, upper_bound=None):
        """ Generate mutants for the temporal insertion operator [0].

        For each logical expression of a given formula three mutants
        per operand are created by inserting the temporal operators
        Finally, Globally and Next in front of the operand.

        Examples:
            a is mutated into F(a), G(a) and N(a)
            F(a) is mutated into F(F(a)), F(G(a)) and F(N(a))
            a & b is mutated into F(a) & b, G(a) & b, N(a) & b,
            a & F(b), a & G(b) and a & N(b)

        Args:
            self (Clause) : The formula for which mutants are generated.
            lower_bound (int) : Integer representation of lower bound for newly inserted temporal operators.
            upper_bound (int) : Integer representation of upper bound for newly inserted temporal operators.

        Returns:
            list: Temporal logic formulae that are mutants for the
            temporal insertion operator of the given formula x.

        References:
            [0] : Gordon Fraser and Franz Wotawa, Complementary Criteria for Testing
            Temporal Logic Properties, TAP '09 Proceedings of the 3rd International
            Conference on Tests and Proofs, Pages 58 - 73, 2009.
        """
        pass

    @remove_duplicates
    def ano(self):
        """ Generate mutants for the atomic proposition negation operator
        that is derived from the simple expression negation operator
        of [0].

        For a given formula one mutant is created for each atomic
        proposition by negating the proposition.

        Examples:
            a is mutated into !a
            F(a) is mutated into F(!a)
            a & b is mutated into !a & b and a & !b

        Args:
            self (Clause) : The formula for which mutants are generated.

        Returns:
            list: Temporal logic formulae that are mutants for the
            atomic proposition negation operator of the given formula x.

        References:
            [0] : Black, P.E., Okun, V., Yesha, Y.: Mutation Operators for
            Specifications. In: Proceedings of the Fifteenth IEEE International
            Conference on Automated Software Engineering (ASE 2000), Washington,
            DC, USA. IEEE Computer Society Press, Los Alamitos (2000).
        """
        pass

    @remove_duplicates
    def oro(self, atomic_props):
        """ Generate mutants for the operant replacement operator[0].

        For a given formula mutants are created for each atomic
        proposition by once replacing the proposition with every
        other proposition that is part of the formula.

        Examples:
            a & F(b) is mutated into b & F(b) and a & F(a)
            (a | b) & c is mutated into (c | b) & c, (a | c) & c, (a | b) & a and (a | b) & b

        Args:
            self (Clause) : The formula for which mutants are generated.
            atomic_props (list) : List of atomic propositins of the formula x.

        Returns:
            list: Temporal logic formulae that are mutants for the
            operant replacement operator of the given formula x.

        References:
            [0] : Black, P.E., Okun, V., Yesha, Y.: Mutation Operators for
            Specifications. In: Proceedings of the Fifteenth IEEE International
            Conference on Automated Software Engineering (ASE 2000), Washington,
            DC, USA. IEEE Computer Society Press, Los Alamitos (2000).
        """
        pass

    @remove_duplicates
    def lro(self):
        """ Generate mutants for the logical operator replacement operator[0].

        For a given formula mutants are created for each binary logical
        operator by once replacing the operator with every other existing
        binary logical operator (&, |, ->).

        Examples:
            a & F(b) is mutated into a | F(b) and a -> F(b)
            (a | b) & c is mutated into (a & b) & c, (a -> b) & c, (a | b) | c and (a | b) -> c

        Args:
            self (Clause) : The formula for which mutants are generated.

        Returns:
            list: Temporal logic formulae that are mutants for the
            logical operator replacement operator of the given formula x.

        References:
            [0] : Black, P.E., Okun, V., Yesha, Y.: Mutation Operators for
            Specifications. In: Proceedings of the Fifteenth IEEE International
            Conference on Automated Software Engineering (ASE 2000), Washington,
            DC, USA. IEEE Computer Society Press, Los Alamitos (2000).
        """
        pass

    @remove_duplicates
    def tro(self):
        """ Generate mutants for the temporal operator replacement operator[0].

        For a given formula mutants are created for each temporal
        operator by once replacing the operator with every other existing
        temporal operator that has the same number of operands.

        Examples:
            F(b) is mutated into G(b) and N(b)
            a U b is mutated into a R b
            a U (G b) is mutated into a R (G b), a U (F b) and a U (N b)

        Args:
            self (Clause) : The formula for which mutants are generated.

        Returns:
            list: Temporal logic formulae that are mutants for the
            temporal operator replacement operator of the given formula x.

        References:
            [0] : Gordon Fraser and Franz Wotawa, Complementary Criteria for Testing
            Temporal Logic Properties, TAP '09 Proceedings of the 3rd International
            Conference on Tests and Proofs, Pages 58 - 73, 2009.
        """
        pass

    @remove_duplicates
    def io(self):
        """ Generate mutants for the interval operator.

        For a given formula mutants are created by increasing or decreasing
        the size of the interval for each signal temporal logic operator.

        Examples:
            F[1,2](b) is mutated into F[0,2](b), F[2,2](b), F[1,1](b) and F[1,3](b)
            a U[0,3] b is mutated into a U[1,3] b, a U[0,2] b and a U[0,4] b

        Args:
            self (Clause) : The formula for which mutants are generated.

        Returns:
            list: Temporal logic formulae that are mutants for the
            interval operator of the given formula x.
        """
        pass

    @remove_duplicates
    def eno(self):
        """ Generate mutants for the expression negation operator [0].

        For a given formula one mutant is created for each logical
        expression by negating the expression.

        Examples:
            a & F(b) is mutated into ! (a & F(b)),
            (a | b) & c is mutated into ! ((a | b) & c) and (!(a | b)) & c

        Args:
            self (Clause) : The formula for which mutants are generated.

        Returns:
            list: Temporal logic formulae that are mutants for the
            expression negation operator of the given formula x.

        References:
            [0] : Black, P.E., Okun, V., Yesha, Y.: Mutation Operators for
            Specifications. In: Proceedings of the Fifteenth IEEE International
            Conference on Automated Software Engineering (ASE 2000), Washington,
            DC, USA. IEEE Computer Society Press, Los Alamitos (2000).
        """
        pass

    @remove_duplicates
    def rro(self):
        """ Generate mutants for the relational operator replacement operator [0].

        For a given formula mutants are created for each atomic proposition
        with the format for real numbers, e.g. c^T * x <relational operator> b
        by once replacing the relational operator with every other existing
        relational operator except its exact opposite.

        Examples:
            3x + 4y < 5 is mutated into 3x + 4y <= 5, 3x + 4y == 5,
            3x + 4y != 5 and 3x + 4y > 5

        Args:
            self (Clause) : The formula for which mutants are generated.

        Returns:
            list: Temporal logic formulae that are mutants for the
            relational operator replacement operator of the given formula x.

        References:
            [0] : Black, P.E., Okun, V., Yesha, Y.: Mutation Operators for
            Specifications. In: Proceedings of the Fifteenth IEEE International
            Conference on Automated Software Engineering (ASE 2000), Washington,
            DC, USA. IEEE Computer Society Press, Los Alamitos (2000).
        """
        pass

    @remove_duplicates
    def mco(self):
        """ Generate mutants for the missing condition operator [0].

        For each logical binary expression in a given formula two mutants
        are created that hold either the first or the second operand of the
        logical binary expression in the same place but without the logical
        operator and the respective other operand. Implications generate
        only one mutant that holds the second operator, thus only the
        condition for the implication is missing.

        Examples:
            a | b is mutated into a and b
            a & (b -> c) is mutated into b -> c and a & c

        Args:
            self (Clause) : The formula for which mutants are generated.

        Returns:
            list: Temporal logic formulae that are mutants for the
            relational operator replacement operator of the given formula x.

        References:
            [0] : Black, P.E., Okun, V., Yesha, Y.: Mutation Operators for
            Specifications. In: Proceedings of the Fifteenth IEEE International
            Conference on Automated Software Engineering (ASE 2000), Washington,
            DC, USA. IEEE Computer Society Press, Los Alamitos (2000).
        """
        pass

    @remove_duplicates
    def sto(self, onezero):
        """ Generate mutants for the stuck-at operator [0].

        For a given formula one mutant is created for each atomic
        proposition by replacing the proposition with either True
        if onezero equals 1 or False if onezero equals 0.

        Examples if onezero = 1:
            a is mutated into True
            (a | b) & c is mutated into (True | b) & c, (a | True) & c and (a | b) & True

        Examples if onezero = 0:
            a is mutated into False
            (a | b) & c is mutated into (False | b) & c, (a | False) & c and (a | b) & False

        Args:
            self (Clause) : The formula for which mutants are generated.
            onezero (int) : Either 1 or 0.
                            If it is 1 then stuck-at-one mutants are generated.
                            If it is 0 then stuck-at-zero mutants are generated.

        Returns:
            list: Temporal logic formulae that are mutants for the
            stuck-at operator of the given formula x.

        References:
            [0] : Black, P.E., Okun, V., Yesha, Y.: Mutation Operators for
            Specifications. In: Proceedings of the Fifteenth IEEE International
            Conference on Automated Software Engineering (ASE 2000), Washington,
            DC, USA. IEEE Computer Society Press, Los Alamitos (2000).
        """
        pass

    @remove_duplicates
    def ufc(self, plusminus):
        """ Generates test predicates to distinguish Unique First Causes [0].

        Given a formula and a signal (or trace) for it, we define a clause as the Unique
        First Cause (UFC) if in the first state along the signal (or trace) where the
        formula is (dis-)satisfied, it is (dis-)satisfied because of the specific clause.

        Args:
            self (Clause) : The formula for which UFC test predicates are generated.
            plusminus : Operator object that is either "operator.add" if satisfying UFC's
                        are supposed to be tested for or it is "operator.minus" if
                        dissatisfying UFC's are supposed to be tested for.

        References:
            [0] https://github.com/ec-m/BachelorsThesis/blob/master/thesis.pdf
        """
        return self.ufc_plus() if (plusminus == add) else self.ufc_minus()

    def ufc_plus(self):
        """ Generates test predicates to distinguish Unique First Causes that
        satisfy the formula under test.

        Args:
              self (Clause) : The formula for which the test predicates are generated.
        """
        pass

    def ufc_minus(self):
        """ Generates test predicates to distinguish Unique First Causes that
        dissatisfy the formula under test.

        Args:
              self (Clause) : The formula for which the test predicates are generated.
        """
        pass

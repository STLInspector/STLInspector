import unittest
import operator
import os
from STLInspector.core.temporallogic import *
from STLInspector.core.parsing import *


class TestPARSER(unittest.TestCase):
    def test_simple_ltl(self):
        self.assertEqual(parse('a'), AP("a"))
        self.assertEqual(parse('!a'), NOT(AP("a")))
        self.assertEqual(parse('!(a)'), NOT(AP("a")))
        self.assertEqual(parse('! a'), NOT(AP("a")))
        self.assertEqual(parse('! (a)'), NOT(AP("a")))
        self.assertEqual(parse('N a'), NEXT(AP("a")))
        self.assertEqual(parse('N (a)'), NEXT(AP("a")))
        self.assertEqual(parse('o a'), NEXT(AP("a")))
        self.assertEqual(parse('o (a)'), NEXT(AP("a")))
        self.assertEqual(parse('F a'), FINALLY(AP("a")))
        self.assertEqual(parse('F (a)'), FINALLY(AP("a")))
        self.assertEqual(parse('<> a'), FINALLY(AP("a")))
        self.assertEqual(parse('<> (a)'), FINALLY(AP("a")))
        self.assertEqual(parse('G a'), GLOBALLY(AP("a")))
        self.assertEqual(parse('G (a)'), GLOBALLY(AP("a")))
        self.assertEqual(parse('[] a'), GLOBALLY(AP("a")))
        self.assertEqual(parse('[] (a)'), GLOBALLY(AP("a")))
        self.assertEqual(parse('a&b'), AND(AP("a"), AP("b")))
        self.assertEqual(parse('a & b'), AND(AP("a"), AP("b")))
        self.assertEqual(parse('(a)&(b)'), AND(AP("a"), AP("b")))
        self.assertEqual(parse('(a) & (b)'), AND(AP("a"), AP("b")))
        self.assertEqual(parse('a|b'), OR(AP("a"), AP("b")))
        self.assertEqual(parse('a | b'), OR(AP("a"), AP("b")))
        self.assertEqual(parse('(a)|(b)'), OR(AP("a"), AP("b")))
        self.assertEqual(parse('(a) | (b)'), OR(AP("a"), AP("b")))
        self.assertEqual(parse('a->b'), IMPLIES(AP("a"), AP("b")))
        self.assertEqual(parse('a -> b'), IMPLIES(AP("a"), AP("b")))
        self.assertEqual(parse('(a)->(b)'), IMPLIES(AP("a"), AP("b")))
        self.assertEqual(parse('(a) -> (b)'), IMPLIES(AP("a"), AP("b")))
        self.assertEqual(parse('a U b'), UNTIL(AP("a"), AP("b")))
        self.assertEqual(parse('(a)U(b)'), UNTIL(AP("a"), AP("b")))
        self.assertEqual(parse('(a) U (b)'), UNTIL(AP("a"), AP("b")))
        self.assertEqual(parse('a R b'), RELEASE(AP("a"), AP("b")))
        self.assertEqual(parse('(a)R(b)'), RELEASE(AP("a"), AP("b")))
        self.assertEqual(parse('(a) R (b)'), RELEASE(AP("a"), AP("b")))


    def test_simple_stl(self):
        self.assertEqual(parse('x + 2*y + 3*z <= 42'), AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')))
        self.assertEqual(parse('x + 2*y + 3*z >= 42'), AP(None, (1, 2, 3), operator.ge, 42., ('x', 'y', 'z')))
        self.assertEqual(parse('x + 2*y + 3*z < 42'), AP(None, (1, 2, 3), operator.lt, 42., ('x', 'y', 'z')))
        self.assertEqual(parse('x + 2*y + 3*z > 42'), AP(None, (1, 2, 3), operator.gt, 42., ('x', 'y', 'z')))
        self.assertEqual(parse('x + 2*y + 3*z == 42'), AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')))
        self.assertEqual(parse('x + 2*y + 3*z != 42'), AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')))
        self.assertEqual(parse('x+2*y <= 42'), AP(None, (1, 2), operator.le, 42., ('x', 'y')))
        self.assertEqual(parse('3*x <= 42'), AP(None, [3], operator.le, 42., ['x']))
        self.assertEqual(parse(' 42*y!=42'), AP(None, [42], operator.ne, 42., ['y']))
        self.assertEqual(parse('y >= 42'), AP(None, 1, operator.ge, 42., 'y'))
        self.assertEqual(parse('!x + 2*y + 3*z != 42'), NOT(AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z'))))
        self.assertEqual(parse('! 3*x <= 42'), NOT(AP(None, [3], operator.le, 42., ['x'])))
        self.assertEqual(parse('!(y >= 42)'), NOT(AP(None, 1, operator.ge, 42., ['y'])))
        self.assertEqual(parse('N[42] x + 2*y + 3*z <= 42'),
                         NEXT(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 42))
        self.assertEqual(parse('N[42] (x + 2*y + 3*z <= 42)'),
                         NEXT(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 42))
        self.assertEqual(parse('o[42] x + 2*y + 3*z <= 42'),
                         NEXT(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 42))
        self.assertEqual(parse('o[42] (x + 2*y + 3*z <= 42)'),
                         NEXT(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 42))
        self.assertEqual(parse('F[24, 42] x + 2*y + 3*z <= 42'),
                         FINALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        self.assertEqual(parse('F[24,42] (x + 2*y + 3*z <= 42)'),
                         FINALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        self.assertEqual(parse('<>[24, 42] x + 2*y + 3*z <= 42'),
                         FINALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        self.assertEqual(parse('<>[24,42] (x + 2*y + 3*z <= 42)'),
                         FINALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        self.assertEqual(parse('G[24, 42] x + 2*y + 3*z <= 42'),
                         GLOBALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        self.assertEqual(parse('G[24,42] (x + 2*y + 3*z <= 42)'),
                         GLOBALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        self.assertEqual(parse('[][24, 42] x + 2*y + 3*z <= 42'),
                         GLOBALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        self.assertEqual(parse('[][24,42] (x + 2*y + 3*z <= 42)'),
                         GLOBALLY(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')), 24, 42))
        self.assertEqual(parse('x + 2*y + 3*z == 42& 1*x+2*y<= 42'), AND(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                               AP(None, (1, 2), operator.le, 42., ('x', 'y'))))
        self.assertEqual(parse('3*x <= 42 & y >= 42'),
                         AND(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y'])))
        self.assertEqual(parse('x + 2*y + 3*z == 42|1*x+2*y<= 42'), OR(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                              AP(None, (1, 2), operator.le, 42., ('x', 'y'))))
        self.assertEqual(parse('3*x <= 42 | y >= 42'),
                         OR(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y'])))
        self.assertEqual(parse('x + 2*y + 3*z == 42->1*x+2*y<= 42'),
                         IMPLIES(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                 AP(None, (1, 2), operator.le, 42., ('x', 'y'))))
        self.assertEqual(parse('3*x <= 42 -> y >= 42'),
                         IMPLIES(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y'])))
        self.assertEqual(parse('x + 2*y + 3*z <= 42 U[24, 42] 42*y!=42'), UNTIL(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))
        self.assertEqual(parse('(x + 2*y + 3*z <= 42)U[24,42](42*y!=42)'), UNTIL(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))
        self.assertEqual(parse('(x + 2*y + 3*z <= 42) U[24, 42] (42*y!=42)'), UNTIL(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))
        self.assertEqual(parse('x + 2*y + 3*z <= 42 R[24, 42] 42*y!=42'),
                         RELEASE(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))
        self.assertEqual(parse('(x + 2*y + 3*z <= 42)R[24,42](42*y!=42)'),
                         RELEASE(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))
        self.assertEqual(parse('(x + 2*y + 3*z <= 42) R[24, 42] (42*y!=42)'),
                         RELEASE(AP(None, (1, 2, 3), operator.le, 42., ('x', 'y', 'z')),
                                 AP(None, [42], operator.ne, 42., ['y']), 24, 42))


    def test_nested_ltl(self):
        self.assertEqual(parse('a & b & c'), AND(AND(AP("a"), AP("b")), AP("c")))
        self.assertEqual(parse('a | b | c'), OR(OR(AP("a"), AP("b")), AP("c")))
        self.assertEqual(parse('a & (b | c)'), AND(AP("a"), OR(AP("b"), AP("c"))))
        self.assertEqual(parse('(a | b) & c'), AND(OR(AP("a"), AP("b")), AP("c")))
        self.assertEqual(parse('a & !b & c'), AND(AND(AP("a"), NOT(AP("b"))), AP("c")))
        self.assertEqual(parse('(!(a | b)) & c'), AND(NOT(OR(AP("a"), AP("b"))), AP("c")))
        self.assertEqual(parse('a & !(N b) & c'), AND(AND(AP("a"), NOT(NEXT(AP("b")))), AP("c")))
        self.assertEqual(parse('a U (F b)'), UNTIL(AP("a"), FINALLY(AP("b"))))
        self.assertEqual(parse('a U (G b)'), UNTIL(AP("a"), GLOBALLY(AP("b"))))
        self.assertEqual(parse('a U (N b)'), UNTIL(AP("a"), NEXT(AP("b"))))
        self.assertEqual(parse('(F a) U b'), UNTIL(FINALLY(AP("a")), AP("b")))
        self.assertEqual(parse('(G a) U b'), UNTIL(GLOBALLY(AP("a")), AP("b")))
        self.assertEqual(parse('(N a) U b'), UNTIL(NEXT(AP("a")), AP("b")))
        self.assertEqual(parse('(N a) U (F b)'), UNTIL(NEXT(AP("a")), FINALLY(AP("b"))))
        self.assertEqual(parse('(G a) U (F b)'), UNTIL(GLOBALLY(AP("a")), FINALLY(AP("b"))))
        self.assertEqual(parse('(F a) U (b U c)'), UNTIL(FINALLY(AP("a")), UNTIL(AP("b"), AP("c"))))
        self.assertEqual(parse('(b U c) U (F a)'), UNTIL(UNTIL(AP("b"), AP("c")), FINALLY(AP("a"))))
        self.assertEqual(parse('(x U y) U (b U c)'), UNTIL(UNTIL(AP("x"), AP("y")), UNTIL(AP("b"), AP("c"))))
        self.assertEqual(parse('a R (F b)'), RELEASE(AP("a"), FINALLY(AP("b"))))
        self.assertEqual(parse('a R (G b)'), RELEASE(AP("a"), GLOBALLY(AP("b"))))
        self.assertEqual(parse('a R (N b)'), RELEASE(AP("a"), NEXT(AP("b"))))
        self.assertEqual(parse('(F a) R b'), RELEASE(FINALLY(AP("a")), AP("b")))
        self.assertEqual(parse('(G a) R b'), RELEASE(GLOBALLY(AP("a")), AP("b")))
        self.assertEqual(parse('(N a) R b'), RELEASE(NEXT(AP("a")), AP("b")))
        self.assertEqual(parse('(N a) R (F b)'), RELEASE(NEXT(AP("a")), FINALLY(AP("b"))))
        self.assertEqual(parse('(G a) R (F b)'), RELEASE(GLOBALLY(AP("a")), FINALLY(AP("b"))))
        self.assertEqual(parse('(F a) R (b R c)'), RELEASE(FINALLY(AP("a")), RELEASE(AP("b"), AP("c"))))
        self.assertEqual(parse('(b R c) R (F a)'), RELEASE(RELEASE(AP("b"), AP("c")), FINALLY(AP("a"))))
        self.assertEqual(parse('(x R y) R (b R c)'),
                         RELEASE(RELEASE(AP("x"), AP("y")), RELEASE(AP("b"), AP("c"))))
        self.assertEqual(parse('(x R y) U (b U c)'), UNTIL(RELEASE(AP("x"), AP("y")), UNTIL(AP("b"), AP("c"))))
        self.assertEqual(parse('(x U y) R (b R c)'), RELEASE(UNTIL(AP("x"), AP("y")), RELEASE(AP("b"), AP("c"))))
        self.assertEqual(parse('(x U y) R (b U c)'), RELEASE(UNTIL(AP("x"), AP("y")), UNTIL(AP("b"), AP("c"))))


    def test_nested_stl(self):
        self.assertEqual(parse('x + 2*y + 3*z == 42 & 3*x <= 42 & y >= 42'), AND(AND(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                                   AP(None, [3], operator.le, 42., ['x'])),
                                                                   AP(None, [1], operator.ge, 42., ['y'])))
        self.assertEqual(parse('x + 2*y + 3*z == 42 | 3*x <= 42 | y >= 42'), OR(OR(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                                 AP(None, [3], operator.le, 42., ['x'])),
                                                                 AP(None, [1], operator.ge, 42., ['y'])))
        self.assertEqual(parse('x + 2*y + 3*z == 42 & (3*x <= 42 | y >= 42)'), AND(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                               OR(AP(None, [3], operator.le, 42., ['x']),
                                                                  AP(None, [1], operator.ge, 42., ['y']))))
        self.assertEqual(parse('(x + 2*y + 3*z == 42 | 3*x <= 42) & y >= 42'), AND(
            OR(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), AP(None, [3], operator.le, 42., ['x'])),
            AP(None, [1], operator.ge, 42., ['y'])))
        self.assertEqual(parse('x + 2*y + 3*z == 42 & !3*x <= 42 & y >= 42'), AND(AND(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                                   NOT(AP(None, [3], operator.le, 42., ['x']))),
                                                                   AP(None, [1], operator.ge, 42., ['y'])))
        self.assertEqual(parse('(!(x + 2*y + 3*z == 42 | 3*x <= 42)) & y >= 42'), AND(
            NOT(OR(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), AP(None, [3], operator.le, 42., ['x']))),
            AP(None, [1], operator.ge, 42., ['y'])))
        self.assertEqual(parse('x + 2*y + 3*z == 42 & !(N[11] 3*x <= 42) & y >= 42'), AND(AND(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                                   NOT(
                                                                   NEXT(AP(None, [3], operator.le, 42., ['x']), 11))),
                                                                   AP(None, 1, operator.ge, 42., 'y')))
        self.assertEqual(parse('x + 2*y + 3*z == 42 U[24, 42] (F[3,11] 3*x <= 42)'), UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                                 FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11),
                                                                 24, 42))
        self.assertEqual(parse('x + 2*y + 3*z == 42 U[24, 42] (G[3,11] 3*x <= 42)'), UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                                 GLOBALLY(AP(None, [3], operator.le, 42., ['x']), 3,
                                                                          11), 24, 42))
        self.assertEqual(parse('x + 2*y + 3*z == 42 U[24, 42] (N[11] 3*x <= 42)'), UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                                                 NEXT(AP(None, [3], operator.le, 42., ['x']), 11), 24,
                                                                 42))
        self.assertEqual(parse('(F[3,11] x + 2*y + 3*z == 42) U[24, 42] 3*x <= 42'),
                         UNTIL(FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                               AP(None, [3], operator.le, 42., ['x']), 24, 42))
        self.assertEqual(parse('(G[3,11] x + 2*y + 3*z == 42) U[24, 42] 3*x <= 42'),
                         UNTIL(GLOBALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                               AP(None, [3], operator.le, 42., ['x']), 24, 42))
        self.assertEqual(parse('(N[11] x + 2*y + 3*z == 42) U[24, 42] 3*x <= 42'),
                         UNTIL(NEXT(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 11),
                               AP(None, [3], operator.le, 42., ['x']), 24, 42))
        self.assertEqual(parse('(N[11] x + 2*y + 3*z == 42) U[24, 42] (F[3,11] 3*x <= 42)'),
                         UNTIL(NEXT(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 11),
                               FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 24, 42))
        self.assertEqual(parse('(G[3,11] x + 2*y + 3*z == 42) U[24, 42] (F[3,11] 3*x <= 42)'),
                         UNTIL(GLOBALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                               FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 24, 42))
        self.assertEqual(parse('(F[3,11] x + 2*y + 3*z == 42) U[24, 42] (3*x <= 42 U[24, 42] y >= 42)'),
                         UNTIL(FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                               UNTIL(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y']),
                                     24, 42), 24, 42))
        self.assertEqual(parse('(3*x <= 42 U[24, 42] y >= 42) U[24, 42] (F[3,11] x + 2*y + 3*z == 42)'), UNTIL(
            UNTIL(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y']), 24, 42),
            FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11), 24, 42))
        self.assertEqual(parse('(x + 2*y + 3*z == 42 U[24, 42] x + 2*y + 3*z != 42) U[24, 42] (3*x <= 42 U[24, 42] y >= 42)'), UNTIL(
            UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                  AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')), 24, 42),
            UNTIL(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y']), 24, 42), 24, 42))
        self.assertEqual(parse('x + 2*y + 3*z == 42 R[7,9] (F[3,11] 3*x <= 42)'),
                         RELEASE(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                 FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 7, 9))
        self.assertEqual(parse('x + 2*y + 3*z == 42 R[7,9] (G[3,11] 3*x <= 42)'),
                         RELEASE(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                 GLOBALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 7, 9))
        self.assertEqual(parse('x + 2*y + 3*z == 42 R[7,9] (N[11] 3*x <= 42)'),
                         RELEASE(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                                 NEXT(AP(None, [3], operator.le, 42., ['x']), 11), 7, 9))
        self.assertEqual(parse('(F[3, 11] x + 2*y + 3*z == 42) R[7,9] 3*x <= 42'),
                         RELEASE(FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                                 AP(None, [3], operator.le, 42., ['x']), 7, 9))
        self.assertEqual(parse('(G[3,11] x + 2*y + 3*z == 42) R[7,9] 3*x <= 42'),
                         RELEASE(GLOBALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                                 AP(None, [3], operator.le, 42., ['x']), 7, 9))
        self.assertEqual(parse('(N[11] x + 2*y + 3*z == 42) R[7,9] 3*x <= 42'),
                         RELEASE(NEXT(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 11),
                                 AP(None, [3], operator.le, 42., ['x']), 7, 9))
        self.assertEqual(parse('(N[11] x + 2*y + 3*z == 42) R[7,9] (F[3,11] 3*x <= 42)'),
                         RELEASE(NEXT(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 11),
                                 FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 7, 9))
        self.assertEqual(parse('(G[3,11] x + 2*y + 3*z == 42) R[7,9] (F[3,11] 3*x <= 42)'),
                         RELEASE(GLOBALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                                 FINALLY(AP(None, [3], operator.le, 42., ['x']), 3, 11), 7, 9))
        self.assertEqual(parse('(F[3,11] x + 2*y + 3*z == 42) R[7,9] (3*x <= 42 R[7,9] y >= 42)'),
                         RELEASE(FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11),
                                 RELEASE(AP(None, [3], operator.le, 42., ['x']),
                                         AP(None, 1, operator.ge, 42., ['y']), 7, 9), 7, 9))
        self.assertEqual(parse('(3*x <= 42 R[7,9] y >= 42) R[7,9] (F[3,11] x + 2*y + 3*z == 42)'), RELEASE(
            RELEASE(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y']), 7, 9),
            FINALLY(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')), 3, 11), 7, 9))
        self.assertEqual(parse('(x + 2*y + 3*z == 42 R[7,9] x + 2*y + 3*z != 42) R[7,9] (3*x <= 42 R[7,9] y >= 42)'), RELEASE(
            RELEASE(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                    AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')), 7, 9),
            RELEASE(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y']), 7, 9), 7, 9))
        self.assertEqual(parse('(x + 2*y + 3*z == 42 R[7,9] x + 2*y + 3*z != 42) U[24, 42] (3*x <= 42 U[24, 42] y >= 42)'), UNTIL(
            RELEASE(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                    AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')), 7, 9),
            UNTIL(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y']), 24, 42), 24, 42))
        self.assertEqual(parse('(x + 2*y + 3*z == 42 U[24, 42] x + 2*y + 3*z != 42) R[7,9] (3*x <= 42 R[7,9] y >= 42)'), RELEASE(
            UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                  AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')), 24, 42),
            RELEASE(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y']), 7, 9), 7, 9))
        self.assertEqual(parse('(x + 2*y + 3*z == 42 U[24, 42] x + 2*y + 3*z != 42) R[7,9] (3*x <= 42 U[24, 42] y >= 42)'), RELEASE(
            UNTIL(AP(None, (1, 2, 3), operator.eq, 42., ('x', 'y', 'z')),
                  AP(None, (1, 2, 3), operator.ne, 42., ('x', 'y', 'z')), 24, 42),
            UNTIL(AP(None, [3], operator.le, 42., ['x']), AP(None, 1, operator.ge, 42., ['y']), 24, 42), 7, 9))


    def test_file_parse(self):
        testfile = 'stlinspector.testfile.txt'

        def writeTestFile(formula_str):
            with open(testfile, 'w') as f:
                f.write(formula_str)
        
        writeTestFile('x + 2*y + 3*z <= 42')
        self.assertEqual(parse_from_path(testfile), AP(None, (1, 2, 3), operator.le, 42, ('x', 'y', 'z')))
        
        writeTestFile('x + 2*y + 3*z >= 42')
        self.assertEqual(parse_from_path(testfile), AP(None, (1, 2, 3), operator.ge, 42., ('x', 'y', 'z')))
        
        writeTestFile('G a')
        self.assertEqual(parse_from_path(testfile), GLOBALLY(AP("a")))
        
        writeTestFile('F a')
        self.assertEqual(parse_from_path(testfile), FINALLY(AP("a")))
        
        writeTestFile('N a')
        self.assertEqual(parse_from_path(testfile), NEXT(AP("a")))
        
        writeTestFile('G (a)')
        self.assertEqual(parse_from_path(testfile), GLOBALLY(AP("a")))
        
        writeTestFile('a&b')
        self.assertEqual(parse_from_path(testfile), AND(AP("a"), AP("b")))
        
        writeTestFile('(a) & (b)')
        self.assertEqual(parse_from_path(testfile), AND(AP("a"), AP("b")))
        
        writeTestFile('a | b')
        self.assertEqual(parse_from_path(testfile), OR(AP("a"), AP("b")))
        
        writeTestFile('(a) | (b)')
        self.assertEqual(parse_from_path(testfile), OR(AP("a"), AP("b")))
        
        writeTestFile('a->b')
        self.assertEqual(parse_from_path(testfile), IMPLIES(AP("a"), AP("b")))
        
        writeTestFile('(a) -> (b)')
        self.assertEqual(parse_from_path(testfile), IMPLIES(AP("a"), AP("b")))
        
        writeTestFile('a U b')
        self.assertEqual(parse_from_path(testfile), UNTIL(AP("a"), AP("b")))
        
        writeTestFile('(a)U(b)')
        self.assertEqual(parse_from_path(testfile), UNTIL(AP("a"), AP("b")))
        
        writeTestFile('a R b')
        self.assertEqual(parse_from_path(testfile), RELEASE(AP("a"), AP("b")))
        
        writeTestFile('(a) R (b)')
        self.assertEqual(parse_from_path(testfile), RELEASE(AP("a"), AP("b")))

        if os.path.isfile(testfile):
            os.remove(testfile)


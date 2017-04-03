import unittest
import operator
from core.temporallogic import *


class TestAP(unittest.TestCase):
    def test_str(self):
        self.assertEqual(AP("a").__str__(), "a")
        self.assertEqual(AP("").__str__(), "")
        self.assertEqual(AP(None, (1, 2), operator.ge, 42, ('x', 'y')).__str__(), "(1.0, 2.0)^T (x, y) >= 42")
        self.assertEqual(AP(None, (1, 2), operator.gt, 42, ('x', 'y')).__str__(), "(1.0, 2.0)^T (x, y) > 42")
        self.assertEqual(AP(None, (1, 2), operator.le, 42, ('x', 'y')).__str__(), "(1.0, 2.0)^T (x, y) <= 42")
        self.assertEqual(AP(None, (1, 2), operator.lt, 42, ('x', 'y')).__str__(), "(1.0, 2.0)^T (x, y) < 42")
        self.assertEqual(AP(None, (1, 2), operator.eq, 42, ('x', 'y')).__str__(), "(1.0, 2.0)^T (x, y) == 42")
        self.assertEqual(AP(None, (1, 2), operator.ne, 42, ('x', 'y')).__str__(), "(1.0, 2.0)^T (x, y) != 42")
        self.assertEqual(AP(None, None, operator.ge, 42, ('x', 'y')).__str__(), "(x, y) >= 42")
        self.assertEqual(AP(None, None, operator.ge, 42, 'y').__str__(), "y >= 42")
        self.assertEqual(AP(None).__str__(), "None")

    def test_eq(self):
        self.assertTrue(ap_true == (AP("True")))
        self.assertTrue(ap_false == (AP("False")))
        self.assertFalse(AP("a") == (AP("b")))
        self.assertTrue(AP("a") == (AP("a")))
        self.assertFalse(AP(None, (1, 2), operator.ge, 42, ('x', 'y')) == AP(None, (1, 2), operator.le, 42, ('x', 'y')))
        self.assertFalse(AP(None, (1, 2), operator.ge, 42, ('x', 'y')) == AP(None, (1, 3), operator.ge, 42, ('x', 'y')))
        self.assertFalse(AP(None, (1, 2), operator.ge, 42, ('x', 'y')) == AP(None, (1, 2), operator.ge, 24, ('x', 'y')))
        self.assertFalse(AP(None, (1, 2), operator.ge, 42, ('x', 'y')) == AP(None, (1, 2), operator.ge, 42, ('x', 'z')))
        self.assertTrue(AP(None, (1, 2), operator.ge, 42, ('x', 'y')) == AP(None, (1, 2), operator.ge, 42, ('x', 'y')))

    def test_expand(self):
        self.assertEqual(AP("a").expand(), AP("a"))
        self.assertEqual(AP(None, (1, 2), operator.ge, 42, ('x', 'y')).expand(),
                         AP(None, (1, 2), operator.ge, 42, ('x', 'y')))

    def test_negationnormalform(self):
        self.assertEqual(ap_true.negationnormalform(), ap_true)
        self.assertEqual(ap_false.negationnormalform(), ap_false)
        self.assertEqual(NOT(ap_true).negationnormalform(), ap_false)
        self.assertEqual(NOT(ap_false).negationnormalform(), ap_true)
        self.assertEqual(AP("a").negationnormalform(), AP("a"))
        self.assertEqual(AP(None, (1, 2), operator.ge, 42, ('x', 'y')).negationnormalform(),
                         AP(None, (1, 2), operator.ge, 42, ('x', 'y')))

    def test_nextnormalform(self):
        self.assertEqual(AP("a").nextnormalform(), AP("a"))
        self.assertEqual(AP(None, (1, 2), operator.ge, 42, ('x', 'y')).nextnormalform(),
                         AP(None, (1, 2), operator.ge, 42, ('x', 'y')))
        self.assertEqual(AP("a").nextnormalform(42), AP("a"))
        self.assertEqual(AP(None, (1, 2), operator.ge, 42, ('x', 'y')).nextnormalform(42),
                         AP(None, (1, 2), operator.ge, 42, ('x', 'y')))

    def test_encode(self):
        self.assertEqual(AP("a").encode(42), ('a___42.0', ['(declare-const a___42.0 Bool)']))
        self.assertEqual(AP("a").encode(), ('a___0.0', ['(declare-const a___0.0 Bool)']))
        self.assertEqual(AP("a").encode(0.5), ('a___0.5', ['(declare-const a___0.5 Bool)']))
        self.assertEqual(AP(None, (1, 2), operator.ge, 42, ('x', 'y')).encode(),
                         ('(>= (+ (* 1.0 x___0.0) (* 2.0 y___0.0)) 42)',
                          ['(declare-const x___0.0 Real)', '(declare-const y___0.0 Real)']))
        self.assertEqual(AP(None, (1, 2), operator.ge, 42, ('x', 'y')).encode(42),
                         ('(>= (+ (* 1.0 x___42.0) (* 2.0 y___42.0)) 42)',
                          ['(declare-const x___42.0 Real)', '(declare-const y___42.0 Real)']))
        self.assertEqual(AP(None, None, operator.ne, 42, ('x', 'y')).encode(),
                         ('(distinct (+ x___0.0 y___0.0) 42)',
                          ['(declare-const x___0.0 Real)', '(declare-const y___0.0 Real)']))
        self.assertEqual(AP(None, None, operator.eq, 42, 'x').encode(),
                         ('(= x___0.0 42)', ['(declare-const x___0.0 Real)']))
        self.assertEqual(AP(None, (3,), gt, 42, 'x').encode(),
                         ('(> (* 3.0 x___0.0) 42)', ['(declare-const x___0.0 Real)']))
        self.assertEqual(AP(None, (3,), gt, 42, 'x').encode(0.5),
                         ('(and (>= (* 3.0 x___0.0) 42) (and (> (* 3.0 x___0.5) 42) (>= (* 3.0 x___1.0) 42)))',
                          ['(declare-const x___0.0 Real)', '(declare-const x___0.5 Real)',
                           '(declare-const x___1.0 Real)']))

    def test_get_aps(self):
        self.assertEqual(AP("a").get_aps(), [AP("a")])
        self.assertEqual(AP(None, (1, 2), operator.ge, 42, ('x', 'y')).get_aps(),
                         [AP(None, (1, 2), operator.ge, 42, ('x', 'y'))])


class TestAND(unittest.TestCase):
    def test_str(self):
        self.assertEqual(AND(AP("a"), AP("b")).__str__(), "(a & b)")
        self.assertEqual(AND(AP(""), AP("")).__str__(), "( & )")
        self.assertEqual(AND(AP("a"), AND(AP("b"), AP("c"))).__str__(), "(a & (b & c))")

    def test_eq(self):
        self.assertTrue(AND(AP("a"), AP("b")) == (AND(AP("a"), AP("b"))))
        self.assertTrue(AND(AP("a"), AP("b")) == (AND(AP("b"), AP("a"))))
        self.assertFalse(AND(AP("a"), AP("b")) == (AND(AP("a"), AP("c"))))
        self.assertFalse(AND(AP("a"), AP("b")) == (AND(AP("c"), AP("b"))))
        self.assertFalse(AND(AP("a"), AP("a")) == (AND(AP("b"), AP("b"))))

    def test_expand(self):
        self.assertEqual(AND(AP("a"), AP("b")).expand(), AND(AP("a"), AP("b")))
        self.assertEqual(AND(AP("a"), AND(AP("b"), AP("c"))).expand(), AND(AP("a"), AND(AP("b"), AP("c"))))
        self.assertEqual(AND(FINALLY(AP("a")), AP("b")).expand(), AND(UNTIL(ap_true, AP("a")), AP("b")))

    def test_negationnormalform(self):
        self.assertEqual(AND(AP("a"), AP("b")).negationnormalform(), AND(AP("a"), AP("b")))
        self.assertEqual(AND(AP("a"), AND(AP("b"), AP("c"))).negationnormalform(), AND(AP("a"), AND(AP("b"), AP("c"))))
        self.assertEqual(AND(AP("a"), NOT(AND(AP("b"), AP("c")))).negationnormalform(),
                         AND(AP("a"), OR(NOT(AP("b")), NOT(AP("c")))))

    def test_nextnormalform(self):
        self.assertEqual(AND(AP("a"), AP("b")).nextnormalform(), AND(AP("a"), AP("b")))
        self.assertEqual(AND(AP("a"), AND(AP("b"), AP("c"))).nextnormalform(), AND(AP("a"), AND(AP("b"), AP("c"))))
        self.assertEqual(AND(AP("a"), AP("b")).nextnormalform(42), AND(AP("a"), AP("b")))
        self.assertEqual(AND(AP("a"), AND(AP("b"), AP("c"))).nextnormalform(42), AND(AP("a"), AND(AP("b"), AP("c"))))

    def test_encode(self):
        self.assertEqual(AND(AP("a"), AP("b")).encode(42),
                         (
                         '(and a___42.0 b___42.0)', ['(declare-const a___42.0 Bool)', '(declare-const b___42.0 Bool)']))
        self.assertEqual(AND(AP("a"), AP("b")).encode(0),
                         ('(and a___0.0 b___0.0)', ['(declare-const a___0.0 Bool)', '(declare-const b___0.0 Bool)']))
        self.assertEqual(AND(AND(AP("a"), AP("c")), AP("b")).encode(),
                         ('(and (and a___0.0 c___0.0) b___0.0)',
                          ['(declare-const a___0.0 Bool)', '(declare-const c___0.0 Bool)',
                           '(declare-const b___0.0 Bool)']))

    def test_get_aps(self):
        self.assertEqual(AND(AP("a"), AP("b")).get_aps(), [AP("a"), AP("b")])
        self.assertEqual(AND(AND(AP("a"), AP("c")), AP("b")).get_aps(), [AP("a"), AP("c"), AP("b")])


class TestOR(unittest.TestCase):
    def test_str(self):
        self.assertEqual(OR(AP("a"), AP("b")).__str__(), "(a | b)")
        self.assertEqual(OR(AP(""), AP("")).__str__(), "( | )")
        self.assertEqual(OR(AP("a"), OR(AP("b"), AP("c"))).__str__(), "(a | (b | c))")

    def test_eq(self):
        self.assertTrue(OR(AP("a"), AP("b")) == (OR(AP("a"), AP("b"))))
        self.assertTrue(OR(AP("a"), AP("b")) == (OR(AP("b"), AP("a"))))
        self.assertFalse(OR(AP("a"), AP("b")) == (OR(AP("a"), AP("c"))))
        self.assertFalse(OR(AP("a"), AP("b")) == (OR(AP("c"), AP("b"))))
        self.assertFalse(OR(AP("a"), AP("a")) == (OR(AP("b"), AP("b"))))

    def test_expand(self):
        self.assertEqual(OR(AP("a"), AP("b")).expand(), OR(AP("a"), AP("b")))
        self.assertEqual(OR(AP("a"), OR(AP("b"), AP("c"))).expand(), OR(AP("a"), OR(AP("b"), AP("c"))))
        self.assertEqual(OR(FINALLY(AP("a")), AP("b")).expand(), OR(UNTIL(ap_true, AP("a")), AP("b")))

    def test_negationnormalform(self):
        self.assertEqual(OR(AP("a"), AP("b")).negationnormalform(), OR(AP("a"), AP("b")))
        self.assertEqual(OR(AP("a"), OR(AP("b"), AP("c"))).negationnormalform(), OR(AP("a"), OR(AP("b"), AP("c"))))
        self.assertEqual(OR(AP("a"), NOT(OR(AP("b"), AP("c")))).negationnormalform(),
                         OR(AP("a"), AND(NOT(AP("b")), NOT(AP("c")))))

    def test_nextnormalform(self):
        self.assertEqual(OR(AP("a"), AP("b")).nextnormalform(), OR(AP("a"), AP("b")))
        self.assertEqual(OR(AP("a"), OR(AP("b"), AP("c"))).nextnormalform(), OR(AP("a"), OR(AP("b"), AP("c"))))
        self.assertEqual(OR(AP("a"), AP("b")).nextnormalform(42), OR(AP("a"), AP("b")))
        self.assertEqual(OR(AP("a"), OR(AP("b"), AP("c"))).nextnormalform(42), OR(AP("a"), OR(AP("b"), AP("c"))))

    def test_encode(self):
        self.assertEqual(OR(AP("a"), AP("b")).encode(42),
                         ('(or a___42.0 b___42.0)', ['(declare-const a___42.0 Bool)', '(declare-const b___42.0 Bool)']))
        self.assertEqual(OR(AP("a"), AP("b")).encode(0),
                         ('(or a___0.0 b___0.0)', ['(declare-const a___0.0 Bool)', '(declare-const b___0.0 Bool)']))
        self.assertEqual(OR(OR(AP("a"), AP("c")), AP("b")).encode(),
                         ('(or (or a___0.0 c___0.0) b___0.0)',
                          ['(declare-const a___0.0 Bool)', '(declare-const c___0.0 Bool)',
                           '(declare-const b___0.0 Bool)']))

    def test_get_aps(self):
        self.assertEqual(OR(AP("a"), AP("b")).get_aps(), [AP("a"), AP("b")])
        self.assertEqual(OR(OR(AP("a"), AP("c")), AP("b")).get_aps(), [AP("a"), AP("c"), AP("b")])


class TestIMPLIES(unittest.TestCase):
    def test_str(self):
        self.assertEqual(IMPLIES(AP("a"), AP("b")).__str__(), "(a -> b)")
        self.assertEqual(IMPLIES(AP(""), AP("")).__str__(), "( -> )")
        self.assertEqual(IMPLIES(AP("a"), IMPLIES(AP("b"), AP("c"))).__str__(), "(a -> (b -> c))")

    def test_eq(self):
        self.assertTrue(IMPLIES(AP("a"), AP("b")) == IMPLIES(AP("a"), AP("b")))
        self.assertFalse(IMPLIES(AP("a"), AP("b")) == IMPLIES(AP("b"), AP("a")))
        self.assertFalse(IMPLIES(AP("a"), AP("b")) == IMPLIES(AP("a"), AP("c")))
        self.assertFalse(IMPLIES(AP("a"), AP("b")) == IMPLIES(AP("c"), AP("b")))
        self.assertFalse(IMPLIES(AP("a"), AP("a")) == IMPLIES(AP("b"), AP("b")))

    def test_expand(self):
        self.assertEqual(IMPLIES(AP("a"), AP("b")).expand(), IMPLIES(AP("a"), AP("b")))
        self.assertEqual(IMPLIES(AP("a"), IMPLIES(AP("b"), AP("c"))).expand(),
                         IMPLIES(AP("a"), IMPLIES(AP("b"), AP("c"))))
        self.assertEqual(IMPLIES(FINALLY(AP("a")), AP("b")).expand(), IMPLIES(UNTIL(ap_true, AP("a")), AP("b")))

    def test_negationnormalform(self):
        self.assertEqual(IMPLIES(AP("a"), AP("b")).negationnormalform(), OR(NOT(AP("a")), AP("b")))
        self.assertEqual(IMPLIES(AP("a"), IMPLIES(AP("b"), AP("c"))).negationnormalform(),
                         OR(NOT(AP("a")), OR(NOT(AP("b")), AP("c"))))
        self.assertEqual(IMPLIES(AP("a"), NOT(IMPLIES(AP("b"), AP("c")))).negationnormalform(),
                         OR(NOT(AP("a")), AND(AP("b"), NOT(AP("c")))))

    def test_nextnormalform(self):
        self.assertEqual(IMPLIES(AP("a"), AP("b")).nextnormalform(), IMPLIES(AP("a"), AP("b")))
        self.assertEqual(IMPLIES(AP("a"), IMPLIES(AP("b"), AP("c"))).nextnormalform(),
                         IMPLIES(AP("a"), IMPLIES(AP("b"), AP("c"))))
        self.assertEqual(IMPLIES(AP("a"), AP("b")).nextnormalform(42), IMPLIES(AP("a"), AP("b")))
        self.assertEqual(IMPLIES(AP("a"), IMPLIES(AP("b"), AP("c"))).nextnormalform(42),
                         IMPLIES(AP("a"), IMPLIES(AP("b"), AP("c"))))

    def test_encode(self):
        self.assertEqual(IMPLIES(AP("a"), AP("b")).encode(42),
                         ('(implies a___42.0 b___42.0)',
                          ['(declare-const a___42.0 Bool)', '(declare-const b___42.0 Bool)']))
        self.assertEqual(IMPLIES(AP("a"), AP("b")).encode(0),
                         (
                         '(implies a___0.0 b___0.0)', ['(declare-const a___0.0 Bool)', '(declare-const b___0.0 Bool)']))
        self.assertEqual(IMPLIES(IMPLIES(AP("a"), AP("c")), AP("b")).encode(),
                         ('(implies (implies a___0.0 c___0.0) b___0.0)',
                          ['(declare-const a___0.0 Bool)', '(declare-const c___0.0 Bool)',
                           '(declare-const b___0.0 Bool)']))

    def test_get_aps(self):
        self.assertEqual(IMPLIES(AP("a"), AP("b")).get_aps(), [AP("a"), AP("b")])
        self.assertEqual(IMPLIES(IMPLIES(AP("a"), AP("c")), AP("b")).get_aps(), [AP("a"), AP("c"), AP("b")])


class TestNOT(unittest.TestCase):
    def test_str(self):
        self.assertEqual(NOT(AP("a")).__str__(), "(! a)")
        self.assertEqual(NOT(AP("")).__str__(), "(! )")
        self.assertEqual(NOT(NOT(AP("a"))).__str__(), "(! (! a))")

    def test_eq(self):
        self.assertTrue(NOT(AP("a")) == NOT(AP("a")))
        self.assertTrue(NOT(AND(AP("a"), AP("b"))) == NOT(AND(AP("b"), AP("a"))))
        self.assertFalse(NOT(AP("a")) == NOT(AP("b")))
        self.assertFalse(NOT(OR(AP("a"), AP("b"))) == NOT(OR(AP("a"), AP("c"))))

    def test_expand(self):
        self.assertEqual(NOT(AP("a")).expand(), NOT(AP("a")))
        self.assertEqual(NOT(NOT(AP("b"))).expand(), NOT(NOT(AP("b"))))
        self.assertEqual(NOT(FINALLY(AP("a"))).expand(), NOT(UNTIL(ap_true, AP("a"))))

    def test_negationnormalform(self):
        self.assertEqual(NOT(AP("a")).negationnormalform(), NOT(AP("a")))
        self.assertEqual(NOT(NOT(AP("a"))).negationnormalform(), AP("a"))
        self.assertEqual(NOT(NEXT(AP("a"))).negationnormalform(), NEXT(NOT(AP("a"))))
        self.assertEqual(NOT(AP(None, None, operator.ge, 42, 'x')).negationnormalform(),
                         AP(None, None, operator.lt, 42, 'x'))
        self.assertEqual(NOT(AP(None, None, operator.le, 42, 'x')).negationnormalform(),
                         AP(None, None, operator.gt, 42, 'x'))
        self.assertEqual(NOT(AP(None, None, operator.gt, 42, 'x')).negationnormalform(),
                         AP(None, None, operator.le, 42, 'x'))
        self.assertEqual(NOT(AP(None, None, operator.lt, 42, 'x')).negationnormalform(),
                         AP(None, None, operator.ge, 42, 'x'))
        self.assertEqual(NOT(AP(None, None, operator.eq, 42, 'x')).negationnormalform(),
                         AP(None, None, operator.ne, 42, 'x'))
        self.assertEqual(NOT(AP(None, None, operator.ne, 42, 'x')).negationnormalform(),
                         AP(None, None, operator.eq, 42, 'x'))
        self.assertEqual(NOT(AND(AP("a"), AP("b"))).negationnormalform(), OR(NOT(AP("a")), NOT(AP("b"))))
        self.assertEqual(NOT(OR(AP("a"), AP("b"))).negationnormalform(), AND(NOT(AP("a")), NOT(AP("b"))))
        self.assertEqual(NOT(IMPLIES(AP("a"), AP("b"))).negationnormalform(), AND(AP("a"), NOT(AP("b"))))

    def test_nextnormalform(self):
        self.assertEqual(NOT(AP("a")).nextnormalform(), NOT(AP("a")))
        self.assertEqual(NOT(NOT(AP("b"))).nextnormalform(), NOT(NOT(AP("b"))))
        self.assertEqual(NOT(AP("a")).nextnormalform(42), NOT(AP("a")))
        self.assertEqual(NOT(NOT(AP("b"))).nextnormalform(42), NOT(NOT(AP("b"))))

    def test_encode(self):
        self.assertEqual(NOT(AP("a")).encode(42), ('(not a___42.0)', ['(declare-const a___42.0 Bool)']))
        self.assertEqual(NOT(AP("a")).encode(0), ('(not a___0.0)', ['(declare-const a___0.0 Bool)']))
        self.assertEqual(NOT(NOT(AP("a"))).encode(), ('(not (not a___0.0))', ['(declare-const a___0.0 Bool)']))

    def test_get_aps(self):
        self.assertEqual(NOT(AP("a")).get_aps(), [AP("a")])
        self.assertEqual(NOT(NOT(AP("a"))).get_aps(), [AP("a")])


class TestNEXT(unittest.TestCase):
    def test_str(self):
        self.assertEqual(NEXT(AP("a")).__str__(), "(N a)")
        self.assertEqual(NEXT(AP("")).__str__(), "(N )")
        self.assertEqual(NEXT(None).__str__(), "(N None)")
        self.assertEqual(NEXT(AP("a"), 42).__str__(), "(N[42] a)")
        self.assertEqual(NEXT(AP(""), 42).__str__(), "(N[42] )")
        self.assertEqual(NEXT(None, 42).__str__(), "(N[42] None)")

    def test_eq(self):
        self.assertTrue(NEXT(AP("a")) == NEXT(AP("a")))
        self.assertTrue(NEXT(AND(AP("a"), AP("b"))) == NEXT(AND(AP("b"), AP("a"))))
        self.assertFalse(NEXT(AP("a")) == NEXT(AP("b")))
        self.assertFalse(NEXT(OR(AP("a"), AP("b"))) == NEXT(OR(AP("a"), AP("c"))))
        self.assertTrue(NEXT(AP("a"), 42) == NEXT(AP("a"), 42))
        self.assertTrue(NEXT(AND(AP("a"), AP("b")), 42) == NEXT(AND(AP("b"), AP("a")), 42))
        self.assertFalse(NEXT(AP("a"), 42) == NEXT(AP("b"), 42))
        self.assertFalse(NEXT(OR(AP("a"), AP("b")), 42) == NEXT(OR(AP("a"), AP("c")), 42))
        self.assertFalse(NEXT(AP("a"), 42) == NEXT(AP("b"), 24))

    def test_expand(self):
        self.assertEqual(NEXT(AP("a")).expand(), NEXT(AP("a")))
        self.assertEqual(NEXT(NEXT(AP("b"))).expand(), NEXT(NEXT(AP("b"))))
        self.assertEqual(NEXT(FINALLY(AP("a"))).expand(), NEXT(UNTIL(ap_true, AP("a"))))
        self.assertEqual(NEXT(AP("a"), 42).expand(), NEXT(AP("a"), 42))
        self.assertEqual(NEXT(NEXT(AP("b"), 42), 42).expand(), NEXT(NEXT(AP("b"), 42), 42))
        self.assertEqual(NEXT(FINALLY(AP("a"), 24, 42), 42).expand(), NEXT(UNTIL(ap_true, AP("a"), 24, 42), 42))

    def test_negationnormalform(self):
        self.assertEqual(NEXT(AP("a")).negationnormalform(), NEXT(AP("a")))
        self.assertEqual(NEXT(NOT(AP("a"))).negationnormalform(), NEXT(NOT(AP("a"))))
        self.assertEqual(NEXT(NOT(AP(None, None, operator.ge, 42, 'x'))).negationnormalform(),
                         NEXT(AP(None, None, operator.lt, 42, 'x')))

    def test_nextnormalform(self):
        self.assertEqual(NEXT(AP("a")).nextnormalform(42), NEXT(AP("a")))
        self.assertEqual(NEXT(NEXT(AP("b"))).nextnormalform(42), NEXT(NEXT(AP("b"))))
        self.assertEqual(NEXT(AP("a"), 42).nextnormalform(), NEXT(AP("a"), 42))
        self.assertEqual(NEXT(NEXT(AP("b"), 42), 42).nextnormalform(), NEXT(NEXT(AP("b"), 42), 42))

    def test_encode(self):
        self.assertEqual(NEXT(AP("a")).encode(42), ('a___43.0', ['(declare-const a___43.0 Bool)']))
        self.assertEqual(NEXT(AP("a")).encode(0), ('a___1.0', ['(declare-const a___1.0 Bool)']))
        self.assertEqual(NEXT(NEXT(AP("a"))).encode(), ('a___2.0', ['(declare-const a___2.0 Bool)']))
        self.assertEqual(NEXT(AP("a"), 3).encode(42), ('a___45.0', ['(declare-const a___45.0 Bool)']))
        self.assertEqual(NEXT(AP("a"), 3).encode(0), ('a___3.0', ['(declare-const a___3.0 Bool)']))
        self.assertEqual(NEXT(NEXT(AP("a"), 3), 3).encode(), ('a___6.0', ['(declare-const a___6.0 Bool)']))

    def test_get_aps(self):
        self.assertEqual(NEXT(AP("a")).get_aps(), [AP("a")])
        self.assertEqual(NEXT(NEXT(AP("a"))).get_aps(), [AP("a")])


class TestFINALLY(unittest.TestCase):
    def test_str(self):
        self.assertEqual(FINALLY(AP("a")).__str__(), "(F a)")
        self.assertEqual(FINALLY(AP("")).__str__(), "(F )")
        self.assertEqual(FINALLY(None).__str__(), "(F None)")
        self.assertEqual(FINALLY(AP("a"), 42).__str__(), "(F[42] a)")
        self.assertEqual(FINALLY(AP(""), 42).__str__(), "(F[42] )")
        self.assertEqual(FINALLY(None, 42).__str__(), "(F[42] None)")

    def test_eq(self):
        self.assertTrue(FINALLY(AP("a")) == FINALLY(AP("a")))
        self.assertTrue(FINALLY(FINALLY(AP("a"))) == FINALLY(FINALLY(AP("a"))))
        self.assertFalse(FINALLY(AP("a")) == FINALLY(AP("b")))
        self.assertFalse(FINALLY(OR(AP("a"), AP("b"))) == FINALLY(OR(AP("a"), AP("c"))))
        self.assertTrue(FINALLY(AP("a"), 42) == FINALLY(AP("a"), 42))
        self.assertTrue(FINALLY(FINALLY(AP("a"), 24), 42) == FINALLY(FINALLY(AP("a"), 24), 42))
        self.assertFalse(FINALLY(AP("a"), 42) == FINALLY(AP("b"), 42))
        self.assertFalse(FINALLY(OR(AP("a"), AP("b")), 42) == FINALLY(OR(AP("a"), AP("c")), 42))
        self.assertFalse(FINALLY(AP("a"), 42) == FINALLY(AP("b"), 24))

    def test_expand(self):
        self.assertEqual(FINALLY(AP("a")).expand(), UNTIL(ap_true, AP("a")))
        self.assertEqual(FINALLY(FINALLY(AP("b"))).expand(), UNTIL(ap_true, UNTIL(ap_true, AP("b"))))
        self.assertEqual(FINALLY(NEXT(AP("a"))).expand(), UNTIL(ap_true, NEXT(AP("a"))))
        self.assertEqual(FINALLY(AP("a"), 24, 42).expand(), UNTIL(ap_true, AP("a"), 24, 42))
        self.assertEqual(FINALLY(FINALLY(AP("b"), 24, 42), 24, 42).expand(),
                         UNTIL(ap_true, UNTIL(ap_true, AP("b"), 24, 42), 24, 42))
        self.assertEqual(FINALLY(NEXT(AP("a"), 42), 24, 42).expand(), UNTIL(ap_true, NEXT(AP("a"), 42), 24, 42))

    def test_get_aps(self):
        self.assertEqual(FINALLY(AP("a")).get_aps(), [AP("a")])
        self.assertEqual(FINALLY(FINALLY(AP("a"))).get_aps(), [AP("a")])


class TestGLOBALLY(unittest.TestCase):
    def test_str(self):
        self.assertEqual(GLOBALLY(AP("a")).__str__(), "(G a)")
        self.assertEqual(GLOBALLY(AP("")).__str__(), "(G )")
        self.assertEqual(GLOBALLY(None).__str__(), "(G None)")
        self.assertEqual(GLOBALLY(AP("a"), 42).__str__(), "(G[42] a)")
        self.assertEqual(GLOBALLY(AP(""), 42).__str__(), "(G[42] )")
        self.assertEqual(GLOBALLY(None, 42).__str__(), "(G[42] None)")

    def test_eq(self):
        self.assertTrue(GLOBALLY(AP("a")) == GLOBALLY(AP("a")))
        self.assertTrue(GLOBALLY(GLOBALLY(AP("a"))) == GLOBALLY(GLOBALLY(AP("a"))))
        self.assertFalse(GLOBALLY(AP("a")) == GLOBALLY(AP("b")))
        self.assertFalse(GLOBALLY(OR(AP("a"), AP("b"))) == GLOBALLY(OR(AP("a"), AP("c"))))
        self.assertTrue(GLOBALLY(AP("a"), 42) == GLOBALLY(AP("a"), 42))
        self.assertTrue(GLOBALLY(GLOBALLY(AP("a"), 24), 42) == GLOBALLY(GLOBALLY(AP("a"), 24), 42))
        self.assertFalse(GLOBALLY(AP("a"), 42) == GLOBALLY(AP("b"), 42))
        self.assertFalse(GLOBALLY(OR(AP("a"), AP("b")), 42) == GLOBALLY(OR(AP("a"), AP("c")), 42))
        self.assertFalse(GLOBALLY(AP("a"), 42) == GLOBALLY(AP("b"), 24))

    def test_expand(self):
        self.assertEqual(GLOBALLY(AP("a")).expand(), NOT(UNTIL(ap_true, NOT(AP("a")))))
        self.assertEqual(GLOBALLY(GLOBALLY(AP("b"))).expand(),
                         NOT(UNTIL(ap_true, NOT(NOT(UNTIL(ap_true, NOT(AP("b"))))))))
        self.assertEqual(GLOBALLY(NEXT(AP("a"))).expand(), NOT(UNTIL(ap_true, NOT(NEXT(AP("a"))))))
        self.assertEqual(GLOBALLY(AP("a"), 24, 42).expand(), NOT(UNTIL(ap_true, NOT(AP("a")), 24, 42)))
        self.assertEqual(GLOBALLY(GLOBALLY(AP("b"), 24, 42), 24, 42).expand(),
                         NOT(UNTIL(ap_true, NOT(NOT(UNTIL(ap_true, NOT(AP("b")), 24, 42))), 24, 42)))
        self.assertEqual(GLOBALLY(NEXT(AP("a"), 42), 24, 42).expand(),
                         NOT(UNTIL(ap_true, NOT(NEXT(AP("a"), 42)), 24, 42)))

    def test_get_aps(self):
        self.assertEqual(GLOBALLY(AP("a")).get_aps(), [AP("a")])
        self.assertEqual(GLOBALLY(GLOBALLY(AP("a"))).get_aps(), [AP("a")])


class TestRELEASE(unittest.TestCase):
    def test_str(self):
        self.assertEqual(RELEASE(AP("a"), AP("b")).__str__(), "(a R b)")
        self.assertEqual(RELEASE(AP(""), AP("")).__str__(), "( R )")
        self.assertEqual(RELEASE(AP("a"), AP("b"), 24, 42).__str__(), "(a R[24,42] b)")
        self.assertEqual(RELEASE(AP(""), AP(""), 24, 42).__str__(), "( R[24,42] )")

    def test_eq(self):
        self.assertTrue(RELEASE(AP("a"), AP("b")) == RELEASE(AP("a"), AP("b")))
        self.assertTrue(RELEASE(RELEASE(AP("a"), AP("b")), AP("c")) == RELEASE(RELEASE(AP("a"), AP("b")), AP("c")))
        self.assertFalse(RELEASE(AP("a"), AP("b")) == RELEASE(AP("b"), AP("a")))
        self.assertFalse(RELEASE(OR(AP("a"), AP("b")), AP("c")) == RELEASE(OR(AP("a"), AP("c")), AP("b")))
        self.assertTrue(RELEASE(AP("a"), AP("b"), 24, 42) == RELEASE(AP("a"), AP("b"), 24, 42))
        self.assertTrue(
            RELEASE(RELEASE(AP("a"), AP("b"), 0, 24), AP("c"), 24, 42) == RELEASE(RELEASE(AP("a"), AP("b"), 0, 24),
                                                                                  AP("c"), 24, 42))
        self.assertFalse(RELEASE(AP("a"), AP("b"), 24, 42) == RELEASE(AP("b"), AP("b"), 24, 42))
        self.assertFalse(
            RELEASE(OR(AP("a"), AP("b")), AP("b"), 24, 42) == RELEASE(OR(AP("a"), AP("c")), AP("b"), 24, 42))
        self.assertFalse(RELEASE(AP("a"), AP("b"), 24, 42) == RELEASE(AP("b"), AP("b"), 24, 24))

    def test_expand(self):
        self.assertEqual(RELEASE(AP("a"), AP("b")).expand(), NOT(UNTIL(NOT(AP("a")), NOT(AP("b")))))
        self.assertEqual(RELEASE(RELEASE(AP("a"), AP("b")), AP("c")).expand(),
                         NOT(UNTIL(NOT(NOT(UNTIL(NOT(AP("a")), NOT(AP("b"))))), NOT(AP("c")))))
        self.assertEqual(RELEASE(OR(AP("a"), AP("b")), AP("c")).expand(),
                         NOT(UNTIL(NOT(OR(AP("a"), AP("b"))), NOT(AP("c")))))
        self.assertEqual(RELEASE(AP("a"), AP("b"), 24, 42).expand(), NOT(UNTIL(NOT(AP("a")), NOT(AP("b")), 24, 42)))
        self.assertEqual(RELEASE(RELEASE(AP("a"), AP("b"), 0, 24), AP("c"), 24, 42).expand(),
                         NOT(UNTIL(NOT(NOT(UNTIL(NOT(AP("a")), NOT(AP("b")), 0, 24))), NOT(AP("c")), 24, 42)))
        self.assertEqual(RELEASE(OR(AP("a"), AP("b")), AP("c"), 24, 42).expand(),
                         NOT(UNTIL(NOT(OR(AP("a"), AP("b"))), NOT(AP("c")), 24, 42)))

    def test_get_aps(self):
        self.assertEqual(RELEASE(AP("a"), AP("b")).get_aps(), [AP("a"), AP("b")])
        self.assertEqual(RELEASE(RELEASE(AP("a"), AP("b")), AP("c")).get_aps(), [AP("a"), AP("b"), AP("c")])


class TestUNTIL(unittest.TestCase):
    def test_str(self):
        self.assertEqual(UNTIL(AP("a"), AP("b")).__str__(), "(a U b)")
        self.assertEqual(UNTIL(AP(""), AP("")).__str__(), "( U )")
        self.assertEqual(UNTIL(AP("a"), AP("b"), 24, 42).__str__(), "(a U[24,42] b)")
        self.assertEqual(UNTIL(AP(""), AP(""), 24, 42).__str__(), "( U[24,42] )")

    def test_eq(self):
        self.assertTrue(UNTIL(AP("a"), AP("b")) == UNTIL(AP("a"), AP("b")))
        self.assertTrue(UNTIL(UNTIL(AP("a"), AP("b")), AP("c")) == UNTIL(UNTIL(AP("a"), AP("b")), AP("c")))
        self.assertFalse(UNTIL(AP("a"), AP("b")) == UNTIL(AP("b"), AP("a")))
        self.assertFalse(UNTIL(OR(AP("a"), AP("b")), AP("c")) == UNTIL(OR(AP("a"), AP("c")), AP("b")))
        self.assertTrue(UNTIL(AP("a"), AP("b"), 24, 42) == UNTIL(AP("a"), AP("b"), 24, 42))
        self.assertTrue(
            UNTIL(UNTIL(AP("a"), AP("b"), 0, 24), AP("c"), 24, 42) == UNTIL(UNTIL(AP("a"), AP("b"), 0, 24), AP("c"), 24,
                                                                            42))
        self.assertFalse(UNTIL(AP("a"), AP("b"), 24, 42) == UNTIL(AP("b"), AP("b"), 24, 42))
        self.assertFalse(UNTIL(OR(AP("a"), AP("b")), AP("b"), 24, 42) == UNTIL(OR(AP("a"), AP("c")), AP("b"), 24, 42))
        self.assertFalse(UNTIL(AP("a"), AP("b"), 24, 42) == UNTIL(AP("b"), AP("b"), 24, 24))

    def test_expand(self):
        self.assertEqual(UNTIL(AP("a"), AP("b")).expand(), UNTIL(AP("a"), AP("b")))
        self.assertEqual(UNTIL(AP("a"), UNTIL(AP("b"), AP("c"))).expand(), UNTIL(AP("a"), UNTIL(AP("b"), AP("c"))))
        self.assertEqual(UNTIL(FINALLY(AP("a")), AP("b")).expand(), UNTIL(UNTIL(ap_true, AP("a")), AP("b")))
        self.assertEqual(UNTIL(AP("a"), AP("b"), 24, 42).expand(), UNTIL(AP("a"), AP("b"), 24, 42))
        self.assertEqual(UNTIL(AP("a"), UNTIL(AP("b"), AP("c"), 24, 42), 24, 42).expand(),
                         UNTIL(AP("a"), UNTIL(AP("b"), AP("c"), 24, 42), 24, 42))
        self.assertEqual(UNTIL(FINALLY(AP("a")), AP("b"), 24, 42).expand(),
                         UNTIL(UNTIL(ap_true, AP("a")), AP("b"), 24, 42))

    def test_nextnormalform(self):
        self.assertEqual(UNTIL(AP("a"), AP("b"), 0, 0).nextnormalform(), AP("b"))
        self.assertEqual(UNTIL(AP("a"), AP("b"), 0, 1).nextnormalform(),
                         OR(AP("b"), AND(AP("a"), AND(NEXT(AP("a"), 0.5), OR(NEXT(AP("b"), 0.5), NEXT(AP("b"), 1))))))
        self.assertEqual(UNTIL(AP("a"), AP("b"), 1, 2).nextnormalform(), AND(AP("a"), AND(NEXT(AP("a"), 0.5), NEXT(
            OR(AP("b"), AND(AP("a"), AND(NEXT(AP("a"), 0.5), OR(NEXT(AP("b"), 0.5), NEXT(AP("b"), 1))))), 1))))

    def test_get_aps(self):
        self.assertEqual(UNTIL(AP("a"), AP("b")).get_aps(), [AP("a"), AP("b")])
        self.assertEqual(UNTIL(UNTIL(AP("a"), AP("b")), AP("c")).get_aps(), [AP("a"), AP("b"), AP("c")])

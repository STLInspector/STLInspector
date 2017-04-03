import unittest
import operator
from core.temporallogic import *


class TestSTO(unittest.TestCase):
    def test_simple_one(self):
        self.assertEqual(AP("a").sto(1), [ap_true])
        self.assertEqual(NOT(AP("a")).sto(1), [NOT(ap_true)])
        self.assertEqual(NEXT(AP("a")).sto(1), [NEXT(ap_true)])
        self.assertEqual(FINALLY(AP("a")).sto(1), [FINALLY(ap_true)])
        self.assertEqual(GLOBALLY(AP("a")).sto(1), [GLOBALLY(ap_true)])
        self.assertEqual(AND(AP("a"), AP("b")).sto(1), [AND(ap_true, AP("b")), AND(AP("a"), ap_true)])
        self.assertEqual(OR(AP("a"), AP("b")).sto(1), [OR(ap_true, AP("b")), OR(AP("a"), ap_true)])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).sto(1), [IMPLIES(ap_true, AP("b")), IMPLIES(AP("a"), ap_true)])
        self.assertEqual(UNTIL(AP("a"), AP("b")).sto(1), [UNTIL(ap_true, AP("b")), UNTIL(AP("a"), ap_true)])
        self.assertEqual(RELEASE(AP("a"), AP("b")).sto(1), [RELEASE(ap_true, AP("b")), RELEASE(AP("a"), ap_true)])

    def test_nested_one(self):
        self.assertEqual(set(AND(IMPLIES(AP("a"), AP("b")), AP("c")).sto(1)),
                         set([AND(IMPLIES(ap_true, AP("b")), AP("c")), AND(IMPLIES(AP("a"), ap_true), AP("c")),
                              AND(IMPLIES(AP("a"), AP("b")), ap_true)]))
        self.assertEqual(set(AND(IMPLIES(AP("a"), AP("b")), OR(AP("c"), AP("d"))).sto(1)),
                         set([AND(IMPLIES(ap_true, AP("b")), OR(AP("c"), AP("d"))),
                              AND(IMPLIES(AP("a"), ap_true), OR(AP("c"), AP("d"))),
                              AND(IMPLIES(AP("a"), AP("b")), OR(ap_true, AP("d"))),
                              AND(IMPLIES(AP("a"), AP("b")), OR(AP("c"), ap_true))]))
        self.assertEqual(set(AND(AND(AND(AP("a"), AP("b")), AP("c")), AP("d")).sto(1)),
                         set([AND(AND(AND(ap_true, AP("b")), AP("c")), AP("d")),
                              AND(AND(AND(AP("a"), ap_true), AP("c")), AP("d")),
                              AND(AND(AND(AP("a"), AP("b")), ap_true), AP("d")),
                              AND(AND(AND(AP("a"), AP("b")), AP("c")), ap_true)]))

    def test_simple_zero(self):
        self.assertEqual(AP("a").sto(0), [ap_false])
        self.assertEqual(NOT(AP("a")).sto(0), [NOT(ap_false)])
        self.assertEqual(NEXT(AP("a")).sto(0), [NEXT(ap_false)])
        self.assertEqual(FINALLY(AP("a")).sto(0), [FINALLY(ap_false)])
        self.assertEqual(GLOBALLY(AP("a")).sto(0), [GLOBALLY(ap_false)])
        self.assertEqual(AND(AP("a"), AP("b")).sto(0), [AND(ap_false, AP("b")), AND(AP("a"), ap_false)])
        self.assertEqual(OR(AP("a"), AP("b")).sto(0), [OR(ap_false, AP("b")), OR(AP("a"), ap_false)])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).sto(0), [IMPLIES(ap_false, AP("b")), IMPLIES(AP("a"), ap_false)])
        self.assertEqual(UNTIL(AP("a"), AP("b")).sto(0), [UNTIL(ap_false, AP("b")), UNTIL(AP("a"), ap_false)])
        self.assertEqual(RELEASE(AP("a"), AP("b")).sto(0), [RELEASE(ap_false, AP("b")), RELEASE(AP("a"), ap_false)])

    def test_nested_zero(self):
        self.assertEqual(set(AND(IMPLIES(AP("a"), AP("b")), AP("c")).sto(0)),
                         set([AND(IMPLIES(ap_false, AP("b")), AP("c")), AND(IMPLIES(AP("a"), ap_false), AP("c")),
                              AND(IMPLIES(AP("a"), AP("b")), ap_false)]))
        self.assertEqual(set(AND(IMPLIES(AP("a"), AP("b")), OR(AP("c"), AP("d"))).sto(0)),
                         set([AND(IMPLIES(ap_false, AP("b")), OR(AP("c"), AP("d"))),
                              AND(IMPLIES(AP("a"), ap_false), OR(AP("c"), AP("d"))),
                              AND(IMPLIES(AP("a"), AP("b")), OR(ap_false, AP("d"))),
                              AND(IMPLIES(AP("a"), AP("b")), OR(AP("c"), ap_false))]))
        self.assertEqual(set(AND(AND(AND(AP("a"), AP("b")), AP("c")), AP("d")).sto(0)),
                         set([AND(AND(AND(ap_false, AP("b")), AP("c")), AP("d")),
                              AND(AND(AND(AP("a"), ap_false), AP("c")), AP("d")),
                              AND(AND(AND(AP("a"), AP("b")), ap_false), AP("d")),
                              AND(AND(AND(AP("a"), AP("b")), AP("c")), ap_false)]))


class TestMCO(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(AP("a").mco(), [AP("a")])
        self.assertEqual(NOT(AP("a")).mco(), [NOT(AP("a"))])
        self.assertEqual(NEXT(AP("a")).mco(), [NEXT(AP("a"))])
        self.assertEqual(FINALLY(AP("a")).mco(), [FINALLY(AP("a"))])
        self.assertEqual(GLOBALLY(AP("a")).mco(), [GLOBALLY(AP("a"))])
        self.assertEqual(AND(AP("a"), AP("b")).mco(), [AP("b"), AND(AP("a"), AP("b")), AP("a")])
        self.assertEqual(OR(AP("a"), AP("b")).mco(), [AP("b"), OR(AP("a"), AP("b")), AP("a")])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).mco(), [AP("b"), IMPLIES(AP("a"), AP("b"))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).mco(), [UNTIL(AP("a"), AP("b"))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).mco(), [RELEASE(AP("a"), AP("b"))])

    def test_nested(self):
        self.assertEqual(set(AND(IMPLIES(AP("a"), AP("b")), AP("c")).mco()),
                         set([IMPLIES(AP("a"), AP("b")), AND(AP("b"), AP("c")),
                              AND(IMPLIES(AP("a"), AP("b")), AP("c"))]))
        self.assertEqual(set(AND(IMPLIES(AP("a"), AP("b")), OR(AP("c"), AP("d"))).mco()),
                         set([AND(AP("b"), OR(AP("c"), AP("d"))), AND(IMPLIES(AP("a"), AP("b")), OR(AP("c"),
                                                                                                    AP("d"))),
                              AND(IMPLIES(AP("a"), AP("b")), AP("d")), AND(IMPLIES(AP("a"), AP("b")), AP("c"))]))
        self.assertEqual(set(AND(AND(AND(AP("a"), AP("b")), AP("c")), AP("d")).mco()),
                         set([AND(AND(AP("a"), AP("b")), AP("c")), AND(AND(AP("a"), AP("b")), AP("d")), AND(AND(AP("b"),
                                                                                                                AP(
                                                                                                                    "c")),
                                                                                                            AP("d")),
                              AND(AND(AND(AP("a"), AP("b")), AP("c")), AP("d")), AND(AND(AP("a"), AP("c")), AP("d"))]))


# Only for STL
class TestRRO(unittest.TestCase):
    def test_aps(self):
        self.assertEqual(set(AP(None, (42, 42), operator.ge, 42, ("a", "b")).rro()),
                         set([AP(None, (42, 42), operator.gt, 42, ("a", "b")),
                              AP(None, (42, 42), operator.le, 42, ("a", "b")),
                              AP(None, (42, 42), operator.eq, 42, ("a", "b")),
                              AP(None, (42, 42), operator.ne, 42, ("a", "b"))]))
        self.assertEqual(set(AP(None, (42, 42), operator.gt, 42, ("a", "b")).rro()),
                         set([AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                              AP(None, (42, 42), operator.lt, 42, ("a", "b")),
                              AP(None, (42, 42), operator.eq, 42, ("a", "b")),
                              AP(None, (42, 42), operator.ne, 42, ("a", "b"))]))
        self.assertEqual(set(AP(None, (42, 42), operator.le, 42, ("a", "b")).rro()),
                         set([AP(None, (42, 42), operator.lt, 42, ("a", "b")),
                              AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                              AP(None, (42, 42), operator.eq, 42, ("a", "b")),
                              AP(None, (42, 42), operator.ne, 42, ("a", "b"))]))
        self.assertEqual(set(AP(None, (42, 42), operator.lt, 42, ("a", "b")).rro()),
                         set([AP(None, (42, 42), operator.gt, 42, ("a", "b")),
                              AP(None, (42, 42), operator.le, 42, ("a", "b")),
                              AP(None, (42, 42), operator.eq, 42, ("a", "b")),
                              AP(None, (42, 42), operator.ne, 42, ("a", "b"))]))
        self.assertEqual(set(AP(None, (42, 42), operator.eq, 42, ("a", "b")).rro()),
                         set([AP(None, (42, 42), operator.gt, 42, ("a", "b")),
                              AP(None, (42, 42), operator.le, 42, ("a", "b")),
                              AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                              AP(None, (42, 42), operator.lt, 42, ("a", "b"))]))
        self.assertEqual(set(AP(None, (42, 42), operator.ne, 42, ("a", "b")).rro()),
                         set([AP(None, (42, 42), operator.gt, 42, ("a", "b")),
                              AP(None, (42, 42), operator.le, 42, ("a", "b")),
                              AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                              AP(None, (42, 42), operator.lt, 42, ("a", "b"))]))

    def test_formulae(self):
        self.assertEqual(set(NOT(AP(None, (42, 42), operator.ge, 42, ("a", "b"))).rro()),
                         set([NOT(AP(None, (42, 42), operator.gt, 42, ("a", "b"))),
                              NOT(AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                              NOT(AP(None, (42, 42), operator.eq, 42, ("a", "b"))),
                              NOT(AP(None, (42, 42), operator.ne, 42, ("a", "b")))]))
        self.assertEqual(set(NEXT(AP(None, (42, 42), operator.ge, 42, ("a", "b"))).rro()),
                         set([NEXT(AP(None, (42, 42), operator.gt, 42, ("a", "b"))),
                              NEXT(AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                              NEXT(AP(None, (42, 42), operator.eq, 42, ("a", "b"))),
                              NEXT(AP(None, (42, 42), operator.ne, 42, ("a", "b")))]))
        self.assertEqual(set(FINALLY(AP(None, (42, 42), operator.ge, 42, ("a", "b"))).rro()),
                         set([FINALLY(AP(None, (42, 42), operator.gt, 42, ("a", "b"))),
                              FINALLY(AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                              FINALLY(AP(None, (42, 42), operator.eq, 42, ("a", "b"))),
                              FINALLY(AP(None, (42, 42), operator.ne, 42, ("a", "b")))]))
        self.assertEqual(set(GLOBALLY(AP(None, (42, 42), operator.ge, 42, ("a", "b"))).rro()),
                         set([GLOBALLY(AP(None, (42, 42), operator.gt, 42, ("a", "b"))),
                              GLOBALLY(AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                              GLOBALLY(AP(None, (42, 42), operator.eq, 42, ("a", "b"))),
                              GLOBALLY(AP(None, (42, 42), operator.ne, 42, ("a", "b")))]))
        self.assertEqual(set(AND(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                 AP(None, (42, 42), operator.le, 42, ("a", "b"))).rro()),
                         set([
                             AND(AP(None, (42, 42), operator.gt, 42, ("a", "b")),
                                 AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             AND(AP(None, (42, 42), operator.eq, 42, ("a", "b")),
                                 AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             AND(AP(None, (42, 42), operator.ne, 42, ("a", "b")),
                                 AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             AND(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                 AP(None, (42, 42), operator.lt, 42, ("a", "b"))),
                             AND(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                 AP(None, (42, 42), operator.eq, 42, ("a", "b"))),
                             AND(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                 AP(None, (42, 42), operator.ne, 42, ("a", "b")))]))
        self.assertEqual(set(OR(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                AP(None, (42, 42), operator.le, 42, ("a", "b"))).rro()),
                         set([
                             OR(AP(None, (42, 42), operator.gt, 42, ("a", "b")),
                                AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             OR(AP(None, (42, 42), operator.eq, 42, ("a", "b")),
                                AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             OR(AP(None, (42, 42), operator.ne, 42, ("a", "b")),
                                AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             OR(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                AP(None, (42, 42), operator.lt, 42, ("a", "b"))),
                             OR(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                AP(None, (42, 42), operator.eq, 42, ("a", "b"))),
                             OR(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                AP(None, (42, 42), operator.ne, 42, ("a", "b")))]))
        self.assertEqual(set(IMPLIES(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.le, 42, ("a", "b"))).rro()),
                         set([
                             IMPLIES(AP(None, (42, 42), operator.gt, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             IMPLIES(AP(None, (42, 42), operator.eq, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             IMPLIES(AP(None, (42, 42), operator.ne, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             IMPLIES(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.lt, 42, ("a", "b"))),
                             IMPLIES(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.eq, 42, ("a", "b"))),
                             IMPLIES(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.ne, 42, ("a", "b")))]))
        self.assertEqual(set(UNTIL(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                   AP(None, (42, 42), operator.le, 42, ("a", "b"))).rro()),
                         set([
                             UNTIL(AP(None, (42, 42), operator.gt, 42, ("a", "b")),
                                   AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             UNTIL(AP(None, (42, 42), operator.eq, 42, ("a", "b")),
                                   AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             UNTIL(AP(None, (42, 42), operator.ne, 42, ("a", "b")),
                                   AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             UNTIL(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                   AP(None, (42, 42), operator.lt, 42, ("a", "b"))),
                             UNTIL(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                   AP(None, (42, 42), operator.eq, 42, ("a", "b"))),
                             UNTIL(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                   AP(None, (42, 42), operator.ne, 42, ("a", "b")))]))
        self.assertEqual(set(RELEASE(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.le, 42, ("a", "b"))).rro()),
                         set([
                             RELEASE(AP(None, (42, 42), operator.gt, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             RELEASE(AP(None, (42, 42), operator.eq, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             RELEASE(AP(None, (42, 42), operator.ne, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.le, 42, ("a", "b"))),
                             RELEASE(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.lt, 42, ("a", "b"))),
                             RELEASE(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.eq, 42, ("a", "b"))),
                             RELEASE(AP(None, (42, 42), operator.ge, 42, ("a", "b")),
                                     AP(None, (42, 42), operator.ne, 42, ("a", "b")))]))


class TestENO(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(AP("a").eno(), [AP("a")])
        self.assertEqual(NOT(AP("a")).eno(), [AP("a")])
        self.assertEqual(NEXT(AP("a")).eno(), [NEXT(AP("a"))])
        self.assertEqual(FINALLY(AP("a")).eno(), [FINALLY(AP("a"))])
        self.assertEqual(GLOBALLY(AP("a")).eno(), [GLOBALLY(AP("a"))])
        self.assertEqual(AND(AP("a"), AP("b")).eno(), [NOT(AND(AP("a"), AP("b"))), AND(AP("a"), AP("b"))])
        self.assertEqual(OR(AP("a"), AP("b")).eno(), [NOT(OR(AP("a"), AP("b"))), OR(AP("a"), AP("b"))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).eno(), [NOT(IMPLIES(AP("a"), AP("b"))), IMPLIES(AP("a"), AP("b"))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).eno(), [UNTIL(AP("a"), AP("b"))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).eno(), [RELEASE(AP("a"), AP("b"))])

    def test_nested(self):
        self.assertEqual(set(AND(OR(AP("a"), AP("b")), AP("c")).eno()),
                         set([NOT(AND(OR(AP("a"), AP("b")), AP("c"))), AND(NOT(OR(AP("a"), AP("b"))), AP("c")),
                              AND(OR(AP("a"), AP("b")), AP("c"))]))
        self.assertEqual(set(AND(OR(AP("a"), AP("b")), NOT(AP("c"))).eno()),
                         set([NOT(AND(OR(AP("a"), AP("b")), NOT(AP("c")))),
                              AND(NOT(OR(AP("a"), AP("b"))), NOT(AP("c"))), AND(OR(AP("a"), AP("b")), AP("c")),
                              AND(OR(AP("a"), AP("b")), NOT(AP("c")))]))
        self.assertEqual(set(NOT(NOT(NOT(AP("a")))).eno()), set([AP("a")]))


# Only for STL
class TestIO(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(AP("a").io(), [AP("a")])
        self.assertEqual(NOT(AP("a")).io(), [NOT(AP("a"))])
        self.assertEqual(NEXT(AP("a"), 42).io(), [NEXT(AP("a"), 43), NEXT(AP("a"), 41), NEXT(AP("a"), 42)])
        self.assertEqual(FINALLY(AP("a"), 24, 42).io(),
                         [FINALLY(AP("a"), 25, 42), FINALLY(AP("a"), 23, 42), FINALLY(AP("a"), 24, 43),
                          FINALLY(AP("a"), 24, 41), FINALLY(AP("a"), 24, 42)])
        self.assertEqual(GLOBALLY(AP("a"), 24, 42).io(),
                         [GLOBALLY(AP("a"), 25, 42), GLOBALLY(AP("a"), 23, 42), GLOBALLY(AP("a"), 24, 43),
                          GLOBALLY(AP("a"), 24, 41), GLOBALLY(AP("a"), 24, 42)])
        self.assertEqual(AND(AP("a"), AP("b")).io(), [AND(AP("a"), AP("b"))])
        self.assertEqual(OR(AP("a"), AP("b")).io(), [OR(AP("a"), AP("b"))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).io(), [IMPLIES(AP("a"), AP("b"))])
        self.assertEqual(UNTIL(AP("a"), AP("b"), 24, 42).io(),
                         [UNTIL(AP("a"), AP("b"), 25, 42), UNTIL(AP("a"), AP("b"), 24, 43),
                          UNTIL(AP("a"), AP("b"), 24, 41), UNTIL(AP("a"), AP("b"), 23, 42),
                          UNTIL(AP("a"), AP("b"), 24, 42)])
        self.assertEqual(RELEASE(AP("a"), AP("b"), 24, 42).io(),
                         [RELEASE(AP("a"), AP("b"), 25, 42), RELEASE(AP("a"), AP("b"), 24, 43),
                          RELEASE(AP("a"), AP("b"), 24, 41), RELEASE(AP("a"), AP("b"), 23, 42),
                          RELEASE(AP("a"), AP("b"), 24, 42)])

    def test_edges(self):
        self.assertEqual(NEXT(AP("a"), 0).io(), [NEXT(AP("a"), 1), NEXT(AP("a"), 0)])
        self.assertEqual(FINALLY(AP("a"), 0, 42).io(),
                         [FINALLY(AP("a"), 1, 42), FINALLY(AP("a"), 0, 43),
                          FINALLY(AP("a"), 0, 41), FINALLY(AP("a"), 0, 42)])
        self.assertEqual(GLOBALLY(AP("a"), 0, 42).io(),
                         [GLOBALLY(AP("a"), 1, 42), GLOBALLY(AP("a"), 0, 43),
                          GLOBALLY(AP("a"), 0, 41), GLOBALLY(AP("a"), 0, 42)])
        self.assertEqual(UNTIL(AP("a"), AP("b"), 0, 42).io(),
                         [UNTIL(AP("a"), AP("b"), 1, 42), UNTIL(AP("a"), AP("b"), 0, 43),
                          UNTIL(AP("a"), AP("b"), 0, 41), UNTIL(AP("a"), AP("b"), 0, 42)])
        self.assertEqual(RELEASE(AP("a"), AP("b"), 0, 42).io(),
                         [RELEASE(AP("a"), AP("b"), 1, 42), RELEASE(AP("a"), AP("b"), 0, 43),
                          RELEASE(AP("a"), AP("b"), 0, 41), RELEASE(AP("a"), AP("b"), 0, 42)])

    def test_nested(self):
        self.assertEqual(set(UNTIL(NEXT(AP("a"), 1), AP("b"), 2, 3).io()),
                         set([UNTIL(NEXT(AP("a"), 1), AP("b"), 3, 3), UNTIL(NEXT(AP("a"), 1), AP("b"), 2, 4),
                              UNTIL(NEXT(AP("a"), 1), AP("b"), 2, 2),
                              UNTIL(NEXT(AP("a"), 1), AP("b"), 1, 3), UNTIL(NEXT(AP("a"), 2), AP("b"), 2, 3),
                              UNTIL(NEXT(AP("a"), 0), AP("b"), 2, 3), UNTIL(NEXT(AP("a"), 1), AP("b"), 2, 3)]))
        self.assertEqual(set(UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 2), 2, 3), 4, 5).io()),
                         set([UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 2), 2, 3), 5, 5),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 2), 2, 3), 4, 6),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 2), 2, 3), 4, 4),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 2), 2, 3), 3, 5),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 2), 2, 3), 4, 5),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 2), 3, 3), 4, 5),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 2), 2, 4), 4, 5),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 2), 2, 2), 4, 5),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 2), 1, 3), 4, 5),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 2, 2), 2, 3), 4, 5),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 0, 2), 2, 3), 4, 5),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 3), 2, 3), 4, 5),
                              UNTIL(AP("b"), RELEASE(AP("a"), FINALLY(AP("c"), 1, 1), 2, 3), 4, 5)]))


class TestTRO(unittest.TestCase):
    def test_ltl(self):
        self.assertEqual((AP("a")).tro(), [AP("a")])
        self.assertEqual((NOT(AP("a"))).tro(), [NOT(AP("a"))])
        self.assertEqual((NEXT(AP("a"))).tro(), [FINALLY(AP("a")), GLOBALLY(AP("a")), NEXT(AP("a"))])
        self.assertEqual((FINALLY(AP("a"))).tro(), [NEXT(AP("a")), GLOBALLY(AP("a")), FINALLY(AP("a"))])
        self.assertEqual((GLOBALLY(AP("a"))).tro(), [NEXT(AP("a")), FINALLY(AP("a")), GLOBALLY(AP("a"))])
        self.assertEqual((AND(AP("a"), AP("b"))).tro(), [AND(AP("a"), AP("b"))])
        self.assertEqual((OR(AP("a"), AP("b"))).tro(), [OR(AP("a"), AP("b"))])
        self.assertEqual((IMPLIES(AP("a"), AP("b"))).tro(), [IMPLIES(AP("a"), AP("b"))])
        self.assertEqual((UNTIL(AP("a"), AP("b"))).tro(), [RELEASE(AP("a"), AP("b")), UNTIL(AP("a"), AP("b"))])
        self.assertEqual((RELEASE(AP("a"), AP("b"))).tro(), [UNTIL(AP("a"), AP("b")), RELEASE(AP("a"), AP("b"))])

    def test_stl(self):
        self.assertEqual((AP("a")).tro(), [AP("a")])
        self.assertEqual((NOT(AP("a"))).tro(), [NOT(AP("a"))])
        self.assertEqual(NEXT(AP("a"), 42).tro(),
                         [FINALLY(AP("a"), 42, 42), GLOBALLY(AP("a"), 42, 42), NEXT(AP("a"), 42)])
        self.assertEqual(FINALLY(AP("a"), 0, 42).tro(),
                         [NEXT(AP("a"), 42), GLOBALLY(AP("a"), 0, 42), FINALLY(AP("a"), 0, 42)])
        self.assertEqual(GLOBALLY(AP("a"), 0, 42).tro(),
                         [NEXT(AP("a"), 42), FINALLY(AP("a"), 0, 42), GLOBALLY(AP("a"), 0, 42)])
        self.assertEqual((AND(AP("a"), AP("b"))).tro(), [AND(AP("a"), AP("b"))])
        self.assertEqual((OR(AP("a"), AP("b"))).tro(), [OR(AP("a"), AP("b"))])
        self.assertEqual((IMPLIES(AP("a"), AP("b"))).tro(), [IMPLIES(AP("a"), AP("b"))])
        self.assertEqual(UNTIL(AP("a"), AP("b"), 0, 42).tro(),
                         [RELEASE(AP("a"), AP("b"), 0, 42), UNTIL(AP("a"), AP("b"), 0, 42)])
        self.assertEqual(RELEASE(AP("a"), AP("b"), 0, 42).tro(),
                         [UNTIL(AP("a"), AP("b"), 0, 42), RELEASE(AP("a"), AP("b"), 0, 42)])

    def test_nested(self):
        self.assertEqual(set((RELEASE(NEXT(AP("a")), AP("b"))).tro()),
                         set([UNTIL(NEXT(AP("a")), AP("b")), RELEASE(FINALLY(AP("a")), AP("b")),
                              RELEASE(GLOBALLY(AP("a")), AP("b")), RELEASE(NEXT(AP("a")), AP("b"))]))
        self.assertEqual(set((RELEASE(NEXT(AP("a"), 42), AP("b"), 0, 42)).tro()),
                         set([UNTIL(NEXT(AP("a"), 42), AP("b"), 0, 42),
                              RELEASE(FINALLY(AP("a"), 42, 42), AP("b"), 0, 42),
                              RELEASE(GLOBALLY(AP("a"), 42, 42), AP("b"), 0, 42),
                              RELEASE(NEXT(AP("a"), 42), AP("b"), 0, 42)]))
        self.assertEqual(set((RELEASE(NEXT(AP("a"), 42), AP("b"), 0, 42)).tro()),
                         set([UNTIL(NEXT(AP("a"), 42), AP("b"), 0, 42),
                              RELEASE(FINALLY(AP("a"), 42, 42), AP("b"), 0, 42),
                              RELEASE(GLOBALLY(AP("a"), 42, 42), AP("b"), 0, 42),
                              RELEASE(NEXT(AP("a"), 42), AP("b"), 0, 42)]))
        self.assertEqual(set(FINALLY(GLOBALLY(NEXT(AP("a")))).tro()), set([NEXT(GLOBALLY(NEXT(AP("a")))),
                                                                          GLOBALLY(GLOBALLY(NEXT(AP("a")))),
                                                                          FINALLY(NEXT(NEXT(AP("a")))),
                                                                          FINALLY(FINALLY(NEXT(AP("a")))),
                                                                          FINALLY(GLOBALLY(FINALLY(AP("a")))),
                                                                          FINALLY(GLOBALLY(GLOBALLY(AP("a")))),
                                                                          FINALLY(GLOBALLY(NEXT(AP("a"))))]))
        self.assertEqual(set(FINALLY(GLOBALLY(NEXT(AP("a"), 1), 2, 3), 4, 5).tro()),
                         set([NEXT(GLOBALLY(NEXT(AP("a"), 1), 2, 3), 5),
                              GLOBALLY(GLOBALLY(NEXT(AP("a"), 1), 2, 3), 4, 5),
                              FINALLY(NEXT(NEXT(AP("a"), 1), 3), 4, 5), FINALLY(FINALLY(NEXT(AP("a"), 1), 2, 3), 4, 5),
                              FINALLY(GLOBALLY(FINALLY(AP("a"), 1, 1), 2, 3), 4, 5),
                              FINALLY(GLOBALLY(GLOBALLY(AP("a"), 1, 1), 2, 3), 4, 5),
                              FINALLY(GLOBALLY(NEXT(AP("a"), 1), 2, 3), 4, 5)]))


class TestLRO(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(AP("a").lro(), [AP("a")])
        self.assertEqual(NOT(AP("a")).lro(), [NOT(AP("a"))])
        self.assertEqual(NEXT(AP("a")).lro(), [NEXT(AP("a"))])
        self.assertEqual(FINALLY(AP("a")).lro(), [FINALLY(AP("a"))])
        self.assertEqual(GLOBALLY(AP("a")).lro(), [GLOBALLY(AP("a"))])
        self.assertEqual(AND(AP("a"), AP("b")).lro(),
                         [OR(AP("a"), AP("b")), IMPLIES(AP("a"), AP("b")), AND(AP("a"), AP("b"))])
        self.assertEqual(OR(AP("a"), AP("b")).lro(),
                         [AND(AP("a"), AP("b")), IMPLIES(AP("a"), AP("b")), OR(AP("a"), AP("b"))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).lro(),
                         [OR(AP("a"), AP("b")), AND(AP("a"), AP("b")), IMPLIES(AP("a"), AP("b"))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).lro(), [UNTIL(AP("a"), AP("b"))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).lro(), [RELEASE(AP("a"), AP("b"))])

    def test_nested(self):
        self.assertEqual(set(AND(AP("a"), OR(AP("b"), AP("c"))).lro()),
                         set([OR(AP("a"), OR(AP("b"), AP("c"))), IMPLIES(AP("a"), OR(AP("b"), AP("c"))), AND(AP("a"),
                                                                                                             OR(AP("b"),
                                                                                                                AP(
                                                                                                                    "c"))),
                              AND(AP("a"), AND(AP("b"), AP("c"))), AND(AP("a"), IMPLIES(AP("b"), AP("c")))]))
        self.assertEqual(set(UNTIL(AP("a"), OR(AP("b"), AP("c"))).lro()),
                         set([UNTIL(AP("a"), OR(AP("b"), AP("c"))), UNTIL(AP("a"), AND(AP("b"), AP("c"))),
                              UNTIL(AP("a"), IMPLIES(AP("b"), AP("c")))]))
        self.assertEqual(set(UNTIL(AP("a"), RELEASE(AP("b"), GLOBALLY(AP("c")))).lro()),
                         set([UNTIL(AP("a"), RELEASE(AP("b"), GLOBALLY(AP("c"))))]))


class TestORO(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(AP("a").oro([AP("a"), AP("b"), AP("c")]), [AP("b"), AP("c")])
        self.assertEqual(NOT(AP("a")).oro([AP("a"), AP("b"), AP("c")]), [NOT(AP("b")), NOT(AP("c"))])
        self.assertEqual(NEXT(AP("a")).oro([AP("a"), AP("b"), AP("c")]), [NEXT(AP("b")), NEXT(AP("c"))])
        self.assertEqual(FINALLY(AP("a")).oro([AP("a"), AP("b"), AP("c")]), [FINALLY(AP("b")), FINALLY(AP("c"))])
        self.assertEqual(GLOBALLY(AP("a")).oro([AP("a"), AP("b"), AP("c")]), [GLOBALLY(AP("b")), GLOBALLY(AP("c"))])
        self.assertEqual(AND(AP("a"), AP("b")).oro([AP("a"), AP("b"), AP("c")]),
                         [AND(AP("c"), AP("b")), AND(AP("a"), AP("c"))])
        self.assertEqual(OR(AP("a"), AP("b")).oro([AP("a"), AP("b"), AP("c")]),
                         [OR(AP("c"), AP("b")), OR(AP("a"), AP("c"))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).oro([AP("a"), AP("b"), AP("c")]),
                         [IMPLIES(AP("c"), AP("b")), IMPLIES(AP("a"), AP("c"))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).oro([AP("a"), AP("b"), AP("c")]),
                         [UNTIL(AP("c"), AP("b")), UNTIL(AP("a"), AP("c"))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).oro([AP("a"), AP("b"), AP("c")]),
                         [RELEASE(AP("c"), AP("b")), RELEASE(AP("a"), AP("c"))])

    def test_nested(self):
        self.assertEqual(set(AND(AP("a"), OR(AP("b"), AP("c"))).oro([AP("a"), AP("b"), AP("c")])),
                         set([AND(AP("b"), OR(AP("b"), AP("c"))), AND(AP("c"), OR(AP("b"), AP("c"))),
                              AND(AP("a"), OR(AP("a"), AP("c"))), AND(AP("a"), OR(AP("b"), AP("a")))]))
        self.assertEqual(set(UNTIL(AP("a"), OR(AP("b"), AP("c"))).oro([AP("a"), AP("b"), AP("c")])),
                         set([UNTIL(AP("b"), OR(AP("b"), AP("c"))), UNTIL(AP("c"), OR(AP("b"), AP("c"))),
                              UNTIL(AP("a"), OR(AP("a"), AP("c"))), UNTIL(AP("a"), OR(AP("b"), AP("a")))]))
        self.assertEqual(
            set(AND(RELEASE(AP("a"), FINALLY(AP("b"))), OR(AP("b"), AP("c"))).oro([AP("a"), AP("b"), AP("c")])),
            set([AND(RELEASE(AP("b"), FINALLY(AP("b"))), OR(AP("b"), AP("c"))),
                 AND(RELEASE(AP("c"), FINALLY(AP("b"))), OR(AP("b"), AP("c"))),
                 AND(RELEASE(AP("a"), FINALLY(AP("c"))), OR(AP("b"), AP("c"))),
                 AND(RELEASE(AP("a"), FINALLY(AP("a"))), OR(AP("b"), AP("c"))),
                 AND(RELEASE(AP("a"), FINALLY(AP("b"))), OR(AP("a"), AP("c"))),
                 AND(RELEASE(AP("a"), FINALLY(AP("b"))), OR(AP("b"), AP("a")))]))


class TestANO(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(AP("a").ano(), [NOT(AP("a"))])
        self.assertEqual(NOT(AP("a")).ano(), [NOT(NOT(AP("a")))])
        self.assertEqual(NEXT(AP("a")).ano(), [NEXT(NOT(AP("a")))])
        self.assertEqual(FINALLY(AP("a")).ano(), [FINALLY(NOT(AP("a")))])
        self.assertEqual(GLOBALLY(AP("a")).ano(), [GLOBALLY(NOT(AP("a")))])
        self.assertEqual(AND(AP("a"), AP("b")).ano(), [AND(NOT(AP("a")), AP("b")), AND(AP("a"), NOT(AP("b")))])
        self.assertEqual(OR(AP("a"), AP("b")).ano(), [OR(NOT(AP("a")), AP("b")), OR(AP("a"), NOT(AP("b")))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).ano(),
                         [IMPLIES(NOT(AP("a")), AP("b")), IMPLIES(AP("a"), NOT(AP("b")))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).ano(), [UNTIL(NOT(AP("a")), AP("b")), UNTIL(AP("a"), NOT(AP("b")))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).ano(),
                         [RELEASE(NOT(AP("a")), AP("b")), RELEASE(AP("a"), NOT(AP("b")))])

    def test_nested(self):
        self.assertEqual(set(AND(AP("a"), OR(AP("b"), AP("c"))).ano()), set([AND(NOT(AP("a")), OR(AP("b"), AP("c"))),
                                                                            AND(AP("a"), OR(NOT(AP("b")), AP("c"))),
                                                                            AND(AP("a"), OR(AP("b"), NOT(AP("c"))))]))
        self.assertEqual(set(OR(AP("a"), IMPLIES(AP("b"), AP("c"))).ano()),
                         set([OR(NOT(AP("a")), IMPLIES(AP("b"), AP("c"))),
                              OR(AP("a"), IMPLIES(NOT(AP("b")), AP("c"))),
                              OR(AP("a"), IMPLIES(AP("b"), NOT(AP("c"))))]))
        self.assertEqual(set(UNTIL(AP("a"), OR(AP("b"), AP("c"))).ano()), set([UNTIL(NOT(AP("a")), OR(AP("b"), AP("c"))),
                                                                              UNTIL(AP("a"), OR(NOT(AP("b")), AP("c"))),
                                                                              UNTIL(AP("a"),
                                                                                    OR(AP("b"), NOT(AP("c"))))]))
        self.assertEqual(set(AND(RELEASE(AP("b"), AP("c")), OR(AP("b"), AP("c"))).ano()), set([AND(RELEASE(NOT(AP("b")),
                                                                                                          AP("c")),
                                                                                                  OR(AP("b"), AP("c"))),
                                                                                              AND(RELEASE(AP("b"),
                                                                                                          NOT(AP("c"))),
                                                                                                  OR(AP("b"), AP("c"))),
                                                                                              AND(RELEASE(AP("b"),
                                                                                                          AP("c")),
                                                                                                  OR(NOT(AP("b")),
                                                                                                     AP("c"))), AND(
                RELEASE(AP("b"), AP("c")), OR(AP("b"), NOT(AP("c"))))]))


class TestTIO(unittest.TestCase):
    def test_ltl(self):
        self.assertEqual(AP("a").tio(), [FINALLY(AP("a")), GLOBALLY(AP("a")), NEXT(AP("a")), AP("a")])
        self.assertEqual(NOT(AP("a")).tio(),
                         [NOT(FINALLY(AP("a"))), NOT(GLOBALLY(AP("a"))), NOT(NEXT(AP("a"))), NOT(AP("a"))])
        self.assertEqual(NEXT(AP("a")).tio(),
                         [NEXT(FINALLY(AP("a"))), NEXT(GLOBALLY(AP("a"))), NEXT(NEXT(AP("a"))), NEXT(AP("a"))])
        self.assertEqual(FINALLY(AP("a")).tio(),
                         [FINALLY(FINALLY(AP("a"))), FINALLY(GLOBALLY(AP("a"))), FINALLY(NEXT(AP("a"))),
                          FINALLY(AP("a"))])
        self.assertEqual(GLOBALLY(AP("a")).tio(),
                         [GLOBALLY(FINALLY(AP("a"))), GLOBALLY(GLOBALLY(AP("a"))), GLOBALLY(NEXT(AP("a"))),
                          GLOBALLY(AP("a"))])
        self.assertEqual(AND(AP("a"), AP("b")).tio(), [AND(FINALLY(AP("a")), AP("b")), AND(AP("a"), FINALLY(AP("b"))),
                                                      AND(GLOBALLY(AP("a")), AP("b")), AND(AP("a"), GLOBALLY(AP("b"))),
                                                      AND(NEXT(AP("a")), AP("b")), AND(AP("a"), NEXT(AP("b"))),
                                                      AND(AP("a"), AP("b"))])
        self.assertEqual(OR(AP("a"), AP("b")).tio(), [OR(FINALLY(AP("a")), AP("b")), OR(AP("a"), FINALLY(AP("b"))),
                                                     OR(GLOBALLY(AP("a")), AP("b")), OR(AP("a"), GLOBALLY(AP("b"))),
                                                     OR(NEXT(AP("a")), AP("b")), OR(AP("a"), NEXT(AP("b"))),
                                                     OR(AP("a"), AP("b"))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).tio(),
                         [IMPLIES(FINALLY(AP("a")), AP("b")), IMPLIES(AP("a"), FINALLY(AP("b"))),
                          IMPLIES(GLOBALLY(AP("a")), AP("b")), IMPLIES(AP("a"), GLOBALLY(AP("b"))),
                          IMPLIES(NEXT(AP("a")), AP("b")), IMPLIES(AP("a"), NEXT(AP("b"))), IMPLIES(AP("a"), AP("b"))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).tio(),
                         [UNTIL(FINALLY(AP("a")), AP("b")), UNTIL(GLOBALLY(AP("a")), AP("b")),
                          UNTIL(NEXT(AP("a")), AP("b")),
                          UNTIL(AP("a"), AP("b")), UNTIL(AP("a"), FINALLY(AP("b"))), UNTIL(AP("a"), GLOBALLY(AP("b"))),
                          UNTIL(AP("a"), NEXT(AP("b")))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).tio(),
                         [RELEASE(FINALLY(AP("a")), AP("b")), RELEASE(GLOBALLY(AP("a")), AP("b")),
                          RELEASE(NEXT(AP("a")), AP("b")),
                          RELEASE(AP("a"), AP("b")), RELEASE(AP("a"), FINALLY(AP("b"))),
                          RELEASE(AP("a"), GLOBALLY(AP("b"))), RELEASE(AP("a"), NEXT(AP("b")))])

    def test_stl(self):
        self.assertEqual(AP("a").tio(0, 42),
                         [FINALLY(AP("a"), 0, 42), GLOBALLY(AP("a"), 0, 42), NEXT(AP("a"), 42), AP("a")])
        self.assertEqual(NOT(AP("a")).tio(0, 42),
                         [NOT(FINALLY(AP("a"), 0, 42)), NOT(GLOBALLY(AP("a"), 0, 42)), NOT(NEXT(AP("a"), 42)),
                          NOT(AP("a"))])
        self.assertEqual(NEXT(AP("a"), 11).tio(0, 42),
                         [NEXT(FINALLY(AP("a"), 0, 42), 11), NEXT(GLOBALLY(AP("a"), 0, 42), 11),
                          NEXT(NEXT(AP("a"), 42), 11), NEXT(AP("a"), 11)])
        self.assertEqual(FINALLY(AP("a"), 3, 11).tio(0, 42),
                         [FINALLY(FINALLY(AP("a"), 0, 42), 3, 11), FINALLY(GLOBALLY(AP("a"), 0, 42), 3, 11),
                          FINALLY(NEXT(AP("a"), 42), 3, 11), FINALLY(AP("a"), 3, 11)])
        self.assertEqual(GLOBALLY(AP("a"), 3, 11).tio(0, 42),
                         [GLOBALLY(FINALLY(AP("a"), 0, 42), 3, 11), GLOBALLY(GLOBALLY(AP("a"), 0, 42), 3, 11),
                          GLOBALLY(NEXT(AP("a"), 42), 3, 11), GLOBALLY(AP("a"), 3, 11)])
        self.assertEqual(AND(AP("a"), AP("b")).tio(0, 42),
                         [AND(FINALLY(AP("a"), 0, 42), AP("b")), AND(AP("a"), FINALLY(AP("b"), 0, 42)),
                          AND(GLOBALLY(AP("a"), 0, 42), AP("b")), AND(AP("a"), GLOBALLY(AP("b"), 0, 42)),
                          AND(NEXT(AP("a"), 42), AP("b")), AND(AP("a"), NEXT(AP("b"), 42)), AND(AP("a"), AP("b"))])
        self.assertEqual(OR(AP("a"), AP("b")).tio(0, 42),
                         [OR(FINALLY(AP("a"), 0, 42), AP("b")), OR(AP("a"), FINALLY(AP("b"), 0, 42)),
                          OR(GLOBALLY(AP("a"), 0, 42), AP("b")), OR(AP("a"), GLOBALLY(AP("b"), 0, 42)),
                          OR(NEXT(AP("a"), 42), AP("b")), OR(AP("a"), NEXT(AP("b"), 42)), OR(AP("a"), AP("b"))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).tio(0, 42),
                         [IMPLIES(FINALLY(AP("a"), 0, 42), AP("b")), IMPLIES(AP("a"), FINALLY(AP("b"), 0, 42)),
                          IMPLIES(GLOBALLY(AP("a"), 0, 42), AP("b")), IMPLIES(AP("a"), GLOBALLY(AP("b"), 0, 42)),
                          IMPLIES(NEXT(AP("a"), 42), AP("b")), IMPLIES(AP("a"), NEXT(AP("b"), 42)),
                          IMPLIES(AP("a"), AP("b"))])
        self.assertEqual(UNTIL(AP("a"), AP("b"), 3, 11).tio(0, 42), [UNTIL(FINALLY(AP("a"), 0, 42), AP("b"), 3, 11),
                                                                      UNTIL(GLOBALLY(AP("a"), 0, 42), AP("b"), 3, 11),
                                                                      UNTIL(NEXT(AP("a"), 42), AP("b"), 3, 11),
                                                                      UNTIL(AP("a"), AP("b"), 3, 11),
                                                                      UNTIL(AP("a"), FINALLY(AP("b"), 0, 42), 3, 11),
                                                                      UNTIL(AP("a"), GLOBALLY(AP("b"), 0, 42), 3, 11),
                                                                      UNTIL(AP("a"), NEXT(AP("b"), 42), 3, 11)])
        self.assertEqual(RELEASE(AP("a"), AP("b"), 3, 11).tio(0, 42),
                         [RELEASE(FINALLY(AP("a"), 0, 42), AP("b"), 3, 11),
                          RELEASE(GLOBALLY(AP("a"), 0, 42), AP("b"), 3, 11), RELEASE(NEXT(AP("a"), 42), AP("b"), 3, 11),
                          RELEASE(AP("a"), AP("b"), 3, 11), RELEASE(AP("a"), FINALLY(AP("b"), 0, 42), 3, 11),
                          RELEASE(AP("a"), GLOBALLY(AP("b"), 0, 42), 3, 11),
                          RELEASE(AP("a"), NEXT(AP("b"), 42), 3, 11)])


class TestMTO(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(AP("a").mto(), [AP("a")])
        self.assertEqual(NOT(AP("a")).mto(), [NOT(AP("a"))])
        self.assertEqual(NEXT(AP("a")).mto(), [AP("a"), NEXT(AP("a"))])
        self.assertEqual(FINALLY(AP("a")).mto(), [AP("a"), FINALLY(AP("a"))])
        self.assertEqual(GLOBALLY(AP("a")).mto(), [AP("a"), GLOBALLY(AP("a"))])
        self.assertEqual(AND(AP("a"), AP("b")).mto(), [AND(AP("a"), AP("b"))])
        self.assertEqual(OR(AP("a"), AP("b")).mto(), [OR(AP("a"), AP("b"))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).mto(), [IMPLIES(AP("a"), AP("b"))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).mto(), [AP("a"), AP("b"), UNTIL(AP("a"), AP("b"))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).mto(), [AP("a"), AP("b"), RELEASE(AP("a"), AP("b"))])

    def test_nested(self):
        self.assertEqual(set(UNTIL(AP("a"), FINALLY(AP("b"))).mto()),
                         set([AP("a"), UNTIL(AP("a"), AP("b")), FINALLY(AP("b")), UNTIL(AP("a"), FINALLY(AP("b")))]))
        self.assertEqual(set(UNTIL(GLOBALLY(AP("b")), AP("a")).mto()),
                         set([AP("a"), UNTIL(AP("b"), AP("a")), GLOBALLY(AP("b")), UNTIL(GLOBALLY(AP("b")), AP("a"))]))
        self.assertEqual(set(UNTIL(AP("a"), RELEASE(AP("b"), AP("c"))).mto()),
                         set([RELEASE(AP("b"), AP("c")), UNTIL(AP("a"), AP("b")), UNTIL(AP("a"), AP("c")), AP("a"),
                              UNTIL(AP("a"), RELEASE(AP("b"), AP("c")))]))
        self.assertEqual(set(RELEASE(AP("a"), UNTIL(AP("b"), AP("c"))).mto()),
                         set([UNTIL(AP("b"), AP("c")), RELEASE(AP("a"), AP("b")), RELEASE(AP("a"), AP("c")), AP("a"),
                              RELEASE(AP("a"), UNTIL(AP("b"), AP("c")))]))
        self.assertEqual(set(FINALLY(GLOBALLY(NEXT(AP("a")))).mto()),
                         set([FINALLY(GLOBALLY(NEXT(AP("a")))), GLOBALLY(NEXT(AP("a"))), FINALLY(NEXT(AP("a"))),
                              FINALLY(GLOBALLY(AP("a")))]))


class TestASO(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(AP("a").aso(), [AP("a")])
        self.assertEqual(NOT(AP("a")).aso(), [NOT(AP("a"))])
        self.assertEqual(NEXT(AP("a")).aso(), [NEXT(AP("a"))])
        self.assertEqual(FINALLY(AP("a")).aso(), [FINALLY(AP("a"))])
        self.assertEqual(GLOBALLY(AP("a")).aso(), [GLOBALLY(AP("a"))])
        self.assertEqual(AND(AP("a"), AP("b")).aso(), [AND(AP("a"), AP("b"))])
        self.assertEqual(OR(AP("a"), AP("b")).aso(), [OR(AP("a"), AP("b"))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).aso(), [IMPLIES(AP("a"), AP("b"))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).aso(), [UNTIL(AP("a"), AP("b"))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).aso(), [RELEASE(AP("a"), AP("b"))])

    def test_nested(self):
        self.assertEqual(set(AND(AP("a"), AND(AP("b"), AP("c"))).aso()), set([AND(AP("a"), AND(AP("b"), AP("c")))]))
        self.assertEqual(set(AND(AP("a"), OR(AP("b"), AP("c"))).aso()),
                         set([AND(AP("a"), OR(AP("b"), AP("c"))), OR(AND(AP("a"), AP("b")), AP("c"))]))
        self.assertEqual(set(OR(AP("a"), AND(AP("b"), AP("c"))).aso()),
                         set([OR(AP("a"), AND(AP("b"), AP("c"))), AND(OR(AP("a"), AP("b")), AP("c"))]))
        self.assertEqual(set(OR(AP("a"), IMPLIES(AP("b"), AP("c"))).aso()),
                         set([OR(AP("a"), IMPLIES(AP("b"), AP("c"))), IMPLIES(OR(AP("a"), AP("b")), AP("c"))]))
        self.assertEqual(set(IMPLIES(AP("a"), AND(AP("b"), AP("c"))).aso()),
                         set([IMPLIES(AP("a"), AND(AP("b"), AP("c"))), AND(IMPLIES(AP("a"), AP("b")), AP("c"))]))
        self.assertEqual(set(UNTIL(AP("a"), RELEASE(AP("b"), AP("c"))).aso()),
                         set([UNTIL(AP("a"), RELEASE(AP("b"), AP("c"))), RELEASE(UNTIL(AP("a"), AP("b")), AP("c"))]))

        self.assertEqual(set(RELEASE(AP("a"), UNTIL(AP("b"), AP("c"))).aso()),
                         set([RELEASE(AP("a"), UNTIL(AP("b"), AP("c"))), UNTIL(RELEASE(AP("a"), AP("b")), AP("c"))]))

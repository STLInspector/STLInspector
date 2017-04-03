import unittest
from core.temporallogic import *


class TestUFCMINUS(unittest.TestCase):

    def test_simple_sub(self):
        self.assertEqual(AP("a").ufc(sub), [NOT(AP("a"))])
        self.assertEqual(NOT(AP("a")).ufc(sub), [AP("a")])
        self.assertEqual(NEXT(AP("a")).ufc(sub), [NEXT(NOT(AP("a")))])
        self.assertEqual(FINALLY(AP("a")).ufc(sub), [UNTIL(NOT(AP("a")), AND(NOT(AP("a")), GLOBALLY(NOT(AP("a")))))])
        self.assertEqual(GLOBALLY(AP("a")).ufc(sub), [UNTIL(AP("a"), NOT(AP("a")))])
        self.assertEqual(AND(AP("a"), AP("b")).ufc(sub), [AND(NOT(AP("a")), AP("b")), AND(AP("a"), NOT(AP("b")))])
        self.assertEqual(OR(AP("a"), AP("b")).ufc(sub), [AND(NOT(AP("a")), NOT(AP("b")))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).ufc(sub),
                         [AND(AP("a"), NOT(AP("b"))), AND(NOT(NOT(AP("a"))), NOT(AP("b")))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).ufc(sub),
                         [UNTIL(AND(AP("a"), NOT(AP("b"))), AND(NOT(AP("a")), NOT(AP("b")))),
                          UNTIL(AND(AP("a"), NOT(AP("b"))), AND(NOT(AP("b")), NOT(UNTIL(AP("a"), AP("b")))))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).ufc(sub),
                         [UNTIL(AND(NOT(AP("a")), NOT(NOT(AP("b")))),
                                AND(AND(NOT(AP("a")), NOT(NOT(AP("b")))), UNTIL(NOT(AP("a")), NOT(AP("b"))))),
                          UNTIL(AND(NOT(AP("a")), NOT(NOT(AP("b")))), NOT(AP("b")))])

    def test_nested_sub(self):
        self.assertEqual(NOT(NOT(AP("a"))).ufc(sub), [NOT(AP("a"))])
        self.assertEqual(NOT(NOT(NOT((AP("a"))))).ufc(sub), [AP("a")])
        self.assertEqual(UNTIL(FINALLY(AP("a")), AP("b")).ufc(sub),
                         [UNTIL(AND(FINALLY(AP("a")), NOT(AP("b"))),
                                AND(UNTIL(NOT(AP("a")), AND(NOT(AP("a")), GLOBALLY(NOT(AP("a"))))),
                                    NOT(AP("b")))), UNTIL(AND(FINALLY(AP("a")), (UNTIL(FINALLY(AP("a")), AP("b")))))])
        self.assertEqual(RELEASE(GLOBALLY(AP("a")), AP("b")).ufc(sub),
                         [UNTIL(AND(NOT(GLOBALLY(AP("a"))), NOT(NOT(AP("b")))),
                                AND(AND(UNTIL(AP("a"), NOT(AP("a"))), NOT(NOT(AP("b")))),
                                    UNTIL(NOT(GLOBALLY(AP("a"))), NOT(AP("b"))))),
                          UNTIL(AND(NOT(GLOBALLY(AP("a"))), NOT(NOT(AP("b")))), NOT(AP("b")))])


class TestUFCPLUS(unittest.TestCase):
    def test_simple_add(self):
        self.assertEqual(AP("a").ufc(add), [AP("a")])
        self.assertEqual(NOT(AP("a")).ufc(add), [NOT(AP("a"))])
        self.assertEqual(NEXT(AP("a")).ufc(add), [NEXT(AP("a"))])
        self.assertEqual(FINALLY(AP("a")).ufc(add), [UNTIL(NOT(AP("a")), AP("a"))])
        self.assertEqual(GLOBALLY(AP("a")).ufc(add), [UNTIL(AP("a"), AND(AP("a"), GLOBALLY(AP("a"))))])
        self.assertEqual(AND(AP("a"), AP("b")).ufc(add), [AND(AP("a"), AP("b"))])
        self.assertEqual(OR(AP("a"), AP("b")).ufc(add), [AND(AP("a"), NOT(AP("b"))), AND(NOT(AP("a")), AP("b"))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).ufc(add),
                         [AND(NOT(AP("a")), NOT(AP("b"))), AND(NOT(NOT(AP("a"))), AP("b"))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).ufc(add),
                         [UNTIL(AND(AP("a"), NOT(AP("b"))),
                                AND(AND(AP("a"), NOT(AP("b"))), UNTIL(AP("a"), AP("b")))),
                          UNTIL(AND(AP("a"), NOT(AP("b"))), AP("b"))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).ufc(add),
                         [UNTIL(AND(NOT(AP("a")), NOT(NOT(AP("b")))),
                                AND(AP("a"), NOT(NOT(AP("b"))))),
                          UNTIL(AND(NOT(AP("a")), NOT(NOT(AP("b")))),
                                AND(AP("b"), NOT(UNTIL(NOT(AP("a")), NOT(AP("b"))))))])

    def test_nested_add(self):
        self.assertEqual(NOT(NOT(AP("a"))).ufc(add), [AP("a")])
        self.assertEqual(NOT(NOT(NOT((AP("a"))))).ufc(add), [NOT(AP("a"))])
        self.assertEqual(UNTIL(FINALLY(AP("a")), AP("b")).ufc(add),
                         [UNTIL(AND(FINALLY(AP("a")), NOT(AP("b"))),
                                AND(AND(UNTIL(NOT(AP("a")), AP("a")), NOT(AP("b"))), UNTIL(FINALLY(AP("a")), AP("b")))),
                          UNTIL(AND(FINALLY(AP("a")), NOT(AP("b"))), AP("b"))])
        self.assertEqual(RELEASE(GLOBALLY(AP("a")), AP("b")).ufc(add),
                         [UNTIL(AND(NOT(GLOBALLY(AP("a"))), NOT(NOT(AP("b")))),
                                AND(UNTIL(AP("a"), AND(AP("a"), GLOBALLY(AP("a")))), NOT(NOT(AP("b"))))),
                          UNTIL(AND(NOT(GLOBALLY(AP("a"))), NOT(NOT(AP("b")))),
                                AND(AP("b"), NOT(UNTIL(NOT(GLOBALLY(AP("a"))), NOT(AP("b"))))))])
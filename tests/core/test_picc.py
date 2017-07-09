import unittest
from STLInspector.core.temporallogic import *


class TestPICC(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(AP("a").picc(), [AP("a"), NOT(AP("a"))])
        self.assertEqual(NOT(AP("a")).picc(), [AP("a"), NOT(AP("a"))])
        self.assertEqual(NEXT(AP("a")).picc(), [NEXT(AP("a")), NEXT(NOT(AP("a")))])
        self.assertEqual(FINALLY(AP("a")).picc(),
                         [UNTIL(NOT(AP("a")), AND(AP("a"), OR(AP("a"), FINALLY(AP("a"))))),
                          UNTIL(NOT(AP("a")), AND(NOT(AP("a")), OR(AP("a"), FINALLY(AP("a")))))])
        self.assertEqual(GLOBALLY(AP("a")).picc(),
                         [UNTIL(AP("a"), AND(AP("a"), GLOBALLY(AP("a")))),
                          UNTIL(AP("a"), AND(NOT(AP("a")), GLOBALLY(AP("a"))))])
        self.assertEqual(AND(AP("a"), AP("b")).picc(),
                         [AND(AP("a"), NOT(AP("b"))), AND(NOT(AP("a")), NOT(AP("b"))), AND(NOT(AP("a")), AP("b"))])
        self.assertEqual(OR(AP("a"), AP("b")).picc(),
                         [AND(AP("a"), AP("b")), AND(NOT(AP("a")), AP("b")), AND(AP("a"), NOT(AP("b")))])
        self.assertEqual(IMPLIES(AP("a"), AP("b")).picc(),
                         [AND(AP("a"), AP("b")), AND(NOT(AP("a")), AP("b")), AND(NOT(AP("a")), NOT(AP("b")))])
        self.assertEqual(UNTIL(AP("a"), AP("b")).picc(),
                         [UNTIL(AND(AP("a"), NOT(AP("b"))), AND(AP("a"), OR(AP("b"), UNTIL(AP("a"), AP("b"))))),
                          UNTIL(AND(AP("a"), NOT(AP("b"))), AND(NOT(AP("a")), OR(AP("b"), UNTIL(AP("a"), AP("b"))))),
                          UNTIL(AND(AP("a"), NOT(AP("b"))), AND(AP("b"), OR(AP("b"), UNTIL(AP("a"), AP("b"))))),
                          UNTIL(AND(AP("a"), NOT(AP("b"))), AND(NOT(AP("b")), OR(AP("b"), UNTIL(AP("a"), AP("b")))))])
        self.assertEqual(RELEASE(AP("a"), AP("b")).picc(),
                         [UNTIL(AND(NOT(AP("a")), NOT(NOT(AP("b")))),
                                AND(AP("a"), OR(NOT(AP("b")), UNTIL(NOT(AP("a")), NOT(AP("b")))))),
                          UNTIL(AND(NOT(AP("a")), NOT(NOT(AP("b")))),
                                AND(NOT(AP("a")), OR(NOT(AP("b")), UNTIL(NOT(AP("a")), NOT(AP("b")))))),
                          UNTIL(AND(NOT(AP("a")), NOT(NOT(AP("b")))),
                                AND(AP("b"), OR(NOT(AP("b")), UNTIL(NOT(AP("a")), NOT(AP("b")))))),
                          UNTIL(AND(NOT(AP("a")), NOT(NOT(AP("b")))),
                                AND(NOT(AP("b")), OR(NOT(AP("b")), UNTIL(NOT(AP("a")), NOT(AP("b"))))))])

    def test_nested(self):
        self.assertEqual(UNTIL(AP("a"), GLOBALLY(AP("b"))).picc(),
                         [UNTIL(AND(AP("a"), NOT(GLOBALLY(AP("b")))),
                                AND(AP("a"), OR(GLOBALLY(AP("b")), UNTIL(AP("a"), GLOBALLY(AP("b")))))),
                          UNTIL(AND(AP("a"), NOT(GLOBALLY(AP("b")))),
                                AND(NOT(AP("a")), OR(GLOBALLY(AP("b")), UNTIL(AP("a"), GLOBALLY(AP("b")))))),
                          UNTIL(AND(AP("a"), NOT(GLOBALLY(AP("b")))),
                                AND(UNTIL(AP("b"), AND(AP("b"), GLOBALLY(AP("b")))),
                                    OR(GLOBALLY(AP("b")), UNTIL(AP("a"), GLOBALLY(AP("b")))))),
                          UNTIL(AND(AP("a"), NOT(GLOBALLY(AP("b")))),
                                AND(UNTIL(AP("b"), AND(NOT(AP("b")), GLOBALLY(AP("b")))),
                                    OR(GLOBALLY(AP("b")), UNTIL(AP("a"), GLOBALLY(AP("b"))))))])
        self.assertEqual(RELEASE(AP("a"), FINALLY(AP("b"))).picc(),
                         [UNTIL(AND(NOT(AP("a")), NOT(NOT(FINALLY(AP("b"))))),
                                AND(AP("a"), OR(NOT(FINALLY(AP("b"))), UNTIL(NOT(AP("a")), NOT(FINALLY(AP("b"))))))),
                          UNTIL(AND(NOT(AP("a")), NOT(NOT(FINALLY(AP("b"))))),
                                AND(NOT(AP("a")), OR(NOT(FINALLY(AP("b"))), UNTIL(NOT(AP("a")), NOT(FINALLY(AP("b"))))))),
                          UNTIL(AND(NOT(AP("a")), NOT(NOT(FINALLY(AP("b"))))),
                                AND(UNTIL(NOT(AP("b")), AND(AP("b"), OR(AP("b"), FINALLY(AP("b"))))),
                                    OR(NOT(FINALLY(AP("b"))), UNTIL(NOT(AP("a")), NOT(FINALLY(AP("b"))))))),
                          UNTIL(AND(NOT(AP("a")), NOT(NOT(FINALLY(AP("b"))))),
                                AND(UNTIL(NOT(AP("b")), AND(NOT(AP("b")), OR(AP("b"), FINALLY(AP("b"))))),
                                    OR(NOT(FINALLY(AP("b"))), UNTIL(NOT(AP("a")), NOT(FINALLY(AP("b")))))))])
        self.assertEqual(NOT(NOT(AP("a"))).picc(), [AP("a"), NOT(AP("a"))])
        self.assertEqual(NOT(NOT(NOT((AP("a"))))).picc(), [AP("a"), NOT(AP("a"))])

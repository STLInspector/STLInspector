import unittest
from STLInspector.frontend.Project import *

class TestTestGeneration(unittest.TestCase):
   def test_happypath(self):
     p = Project("testid")
     p.setStlCandidate("a > 5.0")
     correctResult = {
       'kind': False,
       'finished': False,
       'signals': {u'a': [5.0, 5.0]},
       'step': 1,
       'testId': 0,
       'coverage': 0.0,
       'conflict': False
       }
     testResult = p.testForName("Testy")
     self.assertEqual(testResult, correctResult)

if __name__ == "__main__":
    unittest.main()

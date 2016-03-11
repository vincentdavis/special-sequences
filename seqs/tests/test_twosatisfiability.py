from unittest import TestCase

from seqs.Not import Not
from seqs.TwoSatisfiability import Satisfiable, Forced


class TwoSatTest(TestCase):
    T1 = {1:[2,3], 2:[Not(1),3]}
    T2 = {1:[2], 2:[Not(1)], Not(1):[3], 3:[4,2], 4:[1]}

    def testTwoSat(self):
        """Check that the correct problems are satisfiable."""
        self.assertEqual(Satisfiable(self.T1),True)
        self.assertEqual(Satisfiable(self.T2),False)

    def testForced(self):
        """Check that we can correctly identify forced variables."""
        self.assertEqual(Forced(self.T1),{1:False})
        self.assertEqual(Forced(self.T2),None)

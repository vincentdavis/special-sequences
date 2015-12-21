from unittest import TestCase
from seqs.AcyclicReachability import Reachability

class tes_Reachability(TestCase):
    def test_Reachable(self):
        G = {"A":["C"],"B":["C","D"],"C":["D","E"],"D":[],"E":[]}
        R = Reachability(G)
        for s in "ABCDE":
            for t in "ABCDE":
                self.assertEqual(R.reachable(s,t), s <= t and s+t not in ["AB","DE"])
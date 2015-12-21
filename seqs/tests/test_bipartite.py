from unittest import TestCase
from seqs.Bipartite import isBipartite


class test_Bipartiteness(TestCase):
    def cycle(self,n):
        return {i:[(i-1)%n,(i+1)%n] for i in range(n)}

    def test_EvenCycles(self):
        for i in range(4,12,2):
            self.assertEqual(isBipartite(self.cycle(i)), True)

    def test_OddCycles(self):
        for i in range(3,12,2):
            self.assertEqual(isBipartite(self.cycle(i)), False)

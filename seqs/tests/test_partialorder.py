from unittest import TestCase

from seqs.PartialOrder import isAcyclic, TransitiveClosure, MaximumAntichain, MinimumChainDecomposition


class Test_PartialOrder(TestCase):
    cube = {i:[i^b for b in (1,2,4,8) if i^b > i] for i in range(16)}

    def test_HypercubeAcyclic(self):
        self.assert_(isAcyclic(self.cube))

    def test_HypercubeClosure(self):
        TC = TransitiveClosure(self.cube)
        for i in range(16):
            self.assertEqual(TC[i],
                {j for j in range(16) if i & j == i and i != j})

    def test_HypercubeAntichain(self):
        A = MaximumAntichain(self.cube)
        self.assertEqual(A,{3,5,6,9,10,12})

    def test_HypercubeDilworth(self):
        CD = list(MinimumChainDecomposition(self.cube))
        self.assertEqual(len(CD),6)

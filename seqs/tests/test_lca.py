import random
from unittest import TestCase

from seqs.LCA import RangeMin, LCA, LogarithmicRangeMin, OfflineLCA


class RandomRangeMinTest(TestCase):
    def test_RangeMin(self):
        for trial in range(20):
            data = [random.choice(range(1000000))
                    for i in range(random.randint(1,100))]
            R = RangeMin(data)
            for sample in range(100):
                i = random.randint(0,len(data)-1)
                j = random.randint(i+1,len(data))
                self.assertEqual(R[i:j],min(data[i:j]))

class LCATest(TestCase):
    parent = {'b':'a','c':'a','d':'a','e':'b','f':'b','g':'f','h':'g','i':'g'}
    lcas = {
        ('a','b'):'a',
        ('b','c'):'a',
        ('c','d'):'a',
        ('d','e'):'a',
        ('e','f'):'b',
        ('e','g'):'b',
        ('e','h'):'b',
        ('c','i'):'a',
        ('a','i'):'a',
        ('f','i'):'f',
    }

    def test_LCA(self):
        L = LCA(self.parent)
        for k,v in self.lcas.items():
            self.assertEqual(L(*k),v)

    def test_LogLCA(self):
        L = LCA(self.parent, LogarithmicRangeMin)
        for k,v in self.lcas.items():
            self.assertEqual(L(*k),v)

    def test_OfflineLCA(self):
        L = OfflineLCA(self.parent, self.lcas.keys())
        for (p,q),v in self.lcas.items():
            self.assertEqual(L[p][q],v)

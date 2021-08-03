from unittest import TestCase
from seqs.IntegerHeap import LinearHeap, IntegerHeap
from random import randrange, seed


class test_IntegerHeap(TestCase):
    seed(1234)

    def test_Heaps(self):
        o = 5  # do tests on 2^5-bit integers
        N = LinearHeap()
        I = IntegerHeap(o)
        for iteration in range(20000):
            self.assertEqual(bool(N), bool(I))  # both have same emptiness
            if (not N) or randrange(2):  # flip coin for add/remove
                x = randrange(1 << (1 << o))
                N.add(x)
                I.add(x)
            else:
                x = N.min()
                self.assertEqual(x, I.min())
                N.remove(x)
                I.remove(x)

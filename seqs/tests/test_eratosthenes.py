from unittest import TestCase
from seqs.Eratosthenes import PracticalNumbers

class test_Sieve(TestCase):
    def test_Prime(self):
        """Test that the first few primes are generated correctly."""
        G = primes()
        for p in [2,3,5,7,11,13,17,19,23,29,31,37]:
            self.assertEqual(p,next(G))

    def test_Practical(self):
        """Test that the first few practical nos are generated correctly."""
        G = PracticalNumbers()
        for p in [1,2,4,6,8,12,16,18,20,24,28,30,32,36]:
            self.assertEqual(p,next(G))
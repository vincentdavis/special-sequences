from unittest import TestCase
from seqs.Lyndon import (
    CountLyndonWords,
    LyndonWordsWithLength,
    LengthLimitedLyndonWords,
    isLyndonWord,
    DeBruijnSequence,
)


class test_Lyndon(TestCase):
    def test_Count(self):
        """Test that we count Lyndon words correctly."""
        for s in range(2, 7):
            for n in range(1, 6):
                self.assertEqual(
                    CountLyndonWords(s, n), len(list(LyndonWordsWithLength(s, n)))
                )

    def test_Order(self):
        """Test that we generate Lyndon words in lexicographic order."""
        for s in range(2, 7):
            for n in range(1, 6):
                prev = []
                for x in LengthLimitedLyndonWords(s, n):
                    self.assertTrue(prev < x)
                    prev = list(x)

    def test_Subsequence(self):
        """Test that words of length n-1 are a subsequence of length n."""
        for s in range(2, 7):
            for n in range(2, 6):
                smaller = LengthLimitedLyndonWords(s, n - 1)
                for x in LengthLimitedLyndonWords(s, n):
                    if len(x) < n:
                        self.assertEqual(x, next(smaller))

    def test_IsLyndon(self):
        """Test that the words we generate are Lyndon words."""
        for s in range(2, 7):
            for n in range(2, 6):
                for w in LengthLimitedLyndonWords(s, n):
                    self.assertEqual(isLyndonWord(w), True)

    def test_NotLyndon(self):
        """Test that words that are not Lyndon words aren't claimed to be."""
        nl = sum(1 for i in range(8 ** 4) if isLyndonWord("{0:04o}".format(i)))
        self.assertNotEqual(nl, CountLyndonWords(8, 4))

    def test_DeBruijn(self):
        """Test that the De Bruijn sequence is correct."""
        for s in range(2, 7):
            for n in range(1, 6):
                db = DeBruijnSequence(s, n)
                self.assertEqual(len(db), s ** n)
                db = db + db  # duplicate so we can wrap easier
                subs = set(tuple(db[i : i + n]) for i in range(s ** n))
                self.assertEqual(len(subs), s ** n)

from unittest import TestCase

from seqs.LCS import LongestCommonSubsequence


class LCSTest(TestCase):
    def testLCS(self):
        A = range(10)
        B = reversed(A)
        self.assertEqual(list(A),LongestCommonSubsequence(A,A))
        self.assertEqual(len(LongestCommonSubsequence(A,B)),1)

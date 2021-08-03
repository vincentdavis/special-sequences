from unittest import TestCase
from seqs.Automata import RegularLanguage


class RegExpTest(TestCase):
    # tuples (L,[strings in L],[strings not in L])
    languages = [
        (RegularLanguage("0"), ["0"], ["", "00"]),
        (RegularLanguage("(10+0)*"), ["", "0", "010"], ["1"]),
        (RegularLanguage("(0+1)*1(0+1)(0+1)"), ["000100"], ["0011"]),
    ]

    def test_Membership(self):
        """membership tests for RegularLanguage(expression)"""
        for L, Li, Lx in self.languages:
            for S in Li:
                self.assertTrue(S in L)
            for S in Lx:
                self.assertTrue(S not in L)

    def test_Complement(self):
        """membership tests for ~RegularLanguage"""
        for L, Li, Lx in self.languages:
            L = ~L
            for S in Lx:
                self.assertTrue(S in L)
            for S in Li:
                self.assertTrue(S not in L)

    def test_Equivalent(self):
        """test that converting NFA->expr->NFA produces same language"""
        for L1, Li, Lx in self.languages:
            L2 = RegularLanguage(L1.recognizer.RegExp())
            self.assertEqual(L1, L2)

    def test_Inequivalent(self):
        """test that different regular languages are recognized as different"""
        for i in range(len(self.languages)):
            for j in range(i):
                self.assertNotEqual(self.languages[i][0], self.languages[j][0])

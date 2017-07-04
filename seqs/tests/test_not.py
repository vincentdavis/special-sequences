from unittest import TestCase

from seqs.Not import Not


class NotNotTest(TestCase):
    things = [None,3,"ABC",Not(27)]
    def test_Not(self):
        for x in NotNotTest.things:
            self.assertEqual(Not(Not(x)),x)
    def test_Eq(self):
        for x in NotNotTest.things:
            for y in NotNotTest.things:
                self.assertEqual(Not(x)==Not(y),x==y)
    def test_Hash(self):
        D = {Not(x):x for x in NotNotTest.things}
        for x in NotNotTest.things:
            self.assertEqual(D[Not(x)],x)

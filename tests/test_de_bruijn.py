from unittest import TestCase
from seqs.de_bruijn import de_bruijn, de_bruijn_strings, de_bruijn_bytes
from seqs.Lyndon import DeBruijnSequence


class Test_deBruijnSeq(TestCase):
    # Warning Test result not verified
    seq = "000010002001100120021002201010201110112012101220202110212022102221111211221212222"

    def test_debruijn(self):
        assert de_bruijn(3, 4) == self.seq

    def test_de_bruijn_strings(self):
        assert de_bruijn_strings(3, 4) == self.seq

    def test_de_bruijn_bytes(self):
        assert de_bruijn_bytes(3, 4) == self.seq

    def test_DeBruijnSequence(self):
        assert "".join(str(n) for n in DeBruijnSequence(3, 4)) == self.seq

    def test_DeBruijn(self):
        """Test that the De Bruijn sequence is correct."""
        for s in range(2, 7):
            for n in range(1, 6):
                db = DeBruijnSequence(s, n)
                self.assertEqual(len(db), s ** n)
                db = db + db  # duplicate so we can wrap easier
                subs = set(tuple(db[i : i + n]) for i in range(s ** n))
                self.assertEqual(len(subs), s ** n)

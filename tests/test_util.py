from unittest import TestCase

from seqs.Util import arbitrary_item


class test_arbitrary_item(TestCase):
    def test_arbitrary_list(self):
        s = [1, 2, 3, 4, 5]
        self.assertIn(arbitrary_item(s), s)

    def test_arbitrary_set(self):
        s = {1, 2, 3, 4, 5}
        self.assertIn(arbitrary_item(s), s)

    def test_arbitrary_tuple(self):
        s = (1, 2, 3, 4, 5)
        self.assertIn(arbitrary_item(s), s)

    def test_arbitrary_cardinalitymatching(self):
        """
        I copied a problem "s" from the CubicHam test. This is only testing the first item, there really is no need for ther entire list(dict)
        """
        sbad = {
            (0, 1): {},
            (3, 2): {
                (3, 0): ((3, 2), (3, 0)),
                (3, 1): ((3, 2), (3, 1)),
                (2, 3): ((3, 2), (2, 3)),
            },
            (3, 0): {
                (3, 2): ((3, 0), (3, 2)),
                (3, 1): ((3, 0), (3, 1)),
                (0, 3): ((3, 0), (0, 3)),
            },
            (3, 1): {
                (3, 0): ((3, 1), (3, 0)),
                (3, 2): ((3, 1), (3, 2)),
                (1, 3): ((3, 1), (1, 3)),
            },
            (2, 1): {
                (1, 2): ((2, 1), (1, 2)),
                (2, 0): ((2, 1), (2, 0)),
                (2, 3): ((2, 1), (2, 3)),
            },
            (2, 0): {
                (2, 3): ((2, 0), (2, 3)),
                (0, 2): ((2, 0), (0, 2)),
                (2, 1): ((2, 0), (2, 1)),
            },
            (2, 3): {
                (2, 0): ((2, 3), (2, 0)),
                (3, 2): ((2, 3), (3, 2)),
                (2, 1): ((2, 3), (2, 1)),
            },
            (1, 0): {},
        }
        sgood = {
            (3, 2): {
                (3, 0): ((3, 2), (3, 0)),
                (0, 1): {},
                (3, 1): ((3, 2), (3, 1)),
                (2, 3): ((3, 2), (2, 3)),
            },
            (3, 0): {
                (3, 2): ((3, 0), (3, 2)),
                (3, 1): ((3, 0), (3, 1)),
                (0, 3): ((3, 0), (0, 3)),
            },
            (3, 1): {
                (3, 0): ((3, 1), (3, 0)),
                (3, 2): ((3, 1), (3, 2)),
                (1, 3): ((3, 1), (1, 3)),
            },
            (2, 1): {
                (1, 2): ((2, 1), (1, 2)),
                (2, 0): ((2, 1), (2, 0)),
                (2, 3): ((2, 1), (2, 3)),
            },
            (2, 0): {
                (2, 3): ((2, 0), (2, 3)),
                (0, 2): ((2, 0), (0, 2)),
                (2, 1): ((2, 0), (2, 1)),
            },
            (2, 3): {
                (2, 0): ((2, 3), (2, 0)),
                (3, 2): ((2, 3), (3, 2)),
                (2, 1): ((2, 3), (2, 1)),
            },
            (1, 0): {},
        }
        self.assertIn(arbitrary_item(sgood), sgood)
        self.assertIn(arbitrary_item(sgood[(3, 2)]), sgood)

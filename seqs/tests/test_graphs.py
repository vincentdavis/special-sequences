from unittest import TestCase
from seqs.Graphs import GeneralizedPetersenGraph, GeneralizedCoxeterGraph, LCFNotation


class GraphsTest(TestCase):
    # PetersenGraph = GeneralizedPetersenGraph(5, 2)
    # DesarguesGraph = GeneralizedPetersenGraph(10, 3)
    # CoxeterGraph = GeneralizedCoxeterGraph(7, 2, 3)
    # McGeeGraph = LCFNotation([-12, 7, -7], 8)
    DyckGraph = LCFNotation([-13, 5, -5, 13], 8)
    PappusGraph = LCFNotation([5, 7, -7, 7, -7, -5], 3)
    TutteCoxeterGraph = LCFNotation([-13, -9, 7, -7, 9, 13], 5)
    GrayGraph = LCFNotation([-25, 7, -7, 13, -13, 25], 9)

    def test_PetersenGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(GeneralizedPetersenGraph(5, 2), {(0, False): ((0, True), (3, False), (2, False)),
                                                          (0, True): ((0, False), (4, True), (1, True)),
                                                          (1, False): ((1, True), (4, False), (3, False)),
                                                          (1, True): ((1, False), (0, True), (2, True)),
                                                          (2, False): ((2, True), (0, False), (4, False)),
                                                          (2, True): ((2, False), (1, True), (3, True)),
                                                          (3, False): ((3, True), (1, False), (0, False)),
                                                          (3, True): ((3, False), (2, True), (4, True)),
                                                          (4, False): ((4, True), (2, False), (1, False)),
                                                          (4, True): ((4, False), (3, True), (0, True))}
                         )

    def test_DesarguesGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(GeneralizedPetersenGraph(10, 3), {(0, False): ((0, True), (7, False), (3, False)),
                                                           (0, True): ((0, False), (9, True), (1, True)),
                                                           (1, False): ((1, True), (8, False), (4, False)),
                                                           (1, True): ((1, False), (0, True), (2, True)),
                                                           (2, False): ((2, True), (9, False), (5, False)),
                                                           (2, True): ((2, False), (1, True), (3, True)),
                                                           (3, False): ((3, True), (0, False), (6, False)),
                                                           (3, True): ((3, False), (2, True), (4, True)),
                                                           (4, False): ((4, True), (1, False), (7, False)),
                                                           (4, True): ((4, False), (3, True), (5, True)),
                                                           (5, False): ((5, True), (2, False), (8, False)),
                                                           (5, True): ((5, False), (4, True), (6, True)),
                                                           (6, False): ((6, True), (3, False), (9, False)),
                                                           (6, True): ((6, False), (5, True), (7, True)),
                                                           (7, False): ((7, True), (4, False), (0, False)),
                                                           (7, True): ((7, False), (6, True), (8, True)),
                                                           (8, False): ((8, True), (5, False), (1, False)),
                                                           (8, True): ((8, False), (7, True), (9, True)),
                                                           (9, False): ((9, True), (6, False), (2, False)),
                                                           (9, True): ((9, False), (8, True), (0, True))}
                         )

    def test_CoxeterGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(GeneralizedCoxeterGraph(7, 2, 3), {(0, 0): ((0, 1), (0, 2), (0, 3)),
                                                            (0, 1): ((0, 0), (1, 1), (6, 1)),
                                                            (0, 2): ((0, 0), (2, 2), (5, 2)),
                                                            (0, 3): ((0, 0), (3, 1), (4, 1)),
                                                            (1, 0): ((1, 1), (1, 2), (1, 3)),
                                                            (1, 1): ((1, 0), (2, 1), (0, 1)),
                                                            (1, 2): ((1, 0), (3, 2), (6, 2)),
                                                            (1, 3): ((1, 0), (4, 1), (5, 1)),
                                                            (2, 0): ((2, 1), (2, 2), (2, 3)),
                                                            (2, 1): ((2, 0), (3, 1), (1, 1)),
                                                            (2, 2): ((2, 0), (4, 2), (0, 2)),
                                                            (2, 3): ((2, 0), (5, 1), (6, 1)),
                                                            (3, 0): ((3, 1), (3, 2), (3, 3)),
                                                            (3, 1): ((3, 0), (4, 1), (2, 1)),
                                                            (3, 2): ((3, 0), (5, 2), (1, 2)),
                                                            (3, 3): ((3, 0), (6, 1), (0, 1)),
                                                            (4, 0): ((4, 1), (4, 2), (4, 3)),
                                                            (4, 1): ((4, 0), (5, 1), (3, 1)),
                                                            (4, 2): ((4, 0), (6, 2), (2, 2)),
                                                            (4, 3): ((4, 0), (0, 1), (1, 1)),
                                                            (5, 0): ((5, 1), (5, 2), (5, 3)),
                                                            (5, 1): ((5, 0), (6, 1), (4, 1)),
                                                            (5, 2): ((5, 0), (0, 2), (3, 2)),
                                                            (5, 3): ((5, 0), (1, 1), (2, 1)),
                                                            (6, 0): ((6, 1), (6, 2), (6, 3)),
                                                            (6, 1): ((6, 0), (0, 1), (5, 1)),
                                                            (6, 2): ((6, 0), (1, 2), (4, 2)),
                                                            (6, 3): ((6, 0), (2, 1), (3, 1))}
                         )

    def test_McGeeGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(LCFNotation([-12, 7, -7], 8), {0: (23, 1, 12),
                                                        1: (0, 2, 8),
                                                        2: (1, 3, 19),
                                                        3: (2, 4, 15),
                                                        4: (3, 5, 11),
                                                        5: (4, 6, 22),
                                                        6: (5, 7, 18),
                                                        7: (6, 8, 14),
                                                        8: (7, 9, 1),
                                                        9: (8, 10, 21),
                                                        10: (9, 11, 17),
                                                        11: (10, 12, 4),
                                                        12: (11, 13, 0),
                                                        13: (12, 14, 20),
                                                        14: (13, 15, 7),
                                                        15: (14, 16, 3),
                                                        16: (15, 17, 23),
                                                        17: (16, 18, 10),
                                                        18: (17, 19, 6),
                                                        19: (18, 20, 2),
                                                        20: (19, 21, 13),
                                                        21: (20, 22, 9),
                                                        22: (21, 23, 5),
                                                        23: (22, 0, 16)}
                         )

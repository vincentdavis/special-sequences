from unittest import TestCase
from seqs.Graphs import GeneralizedPetersenGraph, GeneralizedCoxeterGraph, LCFNotation


class GraphsTest(TestCase):
    # PetersenGraph = GeneralizedPetersenGraph(5, 2)
    # DesarguesGraph = GeneralizedPetersenGraph(10, 3)
    # CoxeterGraph = GeneralizedCoxeterGraph(7, 2, 3)
    # McGeeGraph = LCFNotation([-12, 7, -7], 8)
    # DyckGraph = LCFNotation([-13, 5, -5, 13], 8)
    # PappusGraph = LCFNotation([5, 7, -7, 7, -7, -5], 3)
    # TutteCoxeterGraph = LCFNotation([-13, -9, 7, -7, 9, 13], 5)
    GrayGraph = LCFNotation([-25, 7, -7, 13, -13, 25], 9)

    def test_PetersenGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(
            GeneralizedPetersenGraph(5, 2),
            {
                (0, False): ((0, True), (3, False), (2, False)),
                (0, True): ((0, False), (4, True), (1, True)),
                (1, False): ((1, True), (4, False), (3, False)),
                (1, True): ((1, False), (0, True), (2, True)),
                (2, False): ((2, True), (0, False), (4, False)),
                (2, True): ((2, False), (1, True), (3, True)),
                (3, False): ((3, True), (1, False), (0, False)),
                (3, True): ((3, False), (2, True), (4, True)),
                (4, False): ((4, True), (2, False), (1, False)),
                (4, True): ((4, False), (3, True), (0, True)),
            },
        )

    def test_DesarguesGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(
            GeneralizedPetersenGraph(10, 3),
            {
                (0, False): ((0, True), (7, False), (3, False)),
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
                (9, True): ((9, False), (8, True), (0, True)),
            },
        )

    def test_CoxeterGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(
            GeneralizedCoxeterGraph(7, 2, 3),
            {
                (0, 0): ((0, 1), (0, 2), (0, 3)),
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
                (6, 3): ((6, 0), (2, 1), (3, 1)),
            },
        )

    def test_McGeeGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(
            LCFNotation([-12, 7, -7], 8),
            {
                0: (23, 1, 12),
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
                23: (22, 0, 16),
            },
        )

    def test_DyckGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(
            LCFNotation([-13, 5, -5, 13], 8),
            {
                0: (31, 1, 19),
                1: (0, 2, 6),
                2: (1, 3, 29),
                3: (2, 4, 16),
                4: (3, 5, 23),
                5: (4, 6, 10),
                6: (5, 7, 1),
                7: (6, 8, 20),
                8: (7, 9, 27),
                9: (8, 10, 14),
                10: (9, 11, 5),
                11: (10, 12, 24),
                12: (11, 13, 31),
                13: (12, 14, 18),
                14: (13, 15, 9),
                15: (14, 16, 28),
                16: (15, 17, 3),
                17: (16, 18, 22),
                18: (17, 19, 13),
                19: (18, 20, 0),
                20: (19, 21, 7),
                21: (20, 22, 26),
                22: (21, 23, 17),
                23: (22, 24, 4),
                24: (23, 25, 11),
                25: (24, 26, 30),
                26: (25, 27, 21),
                27: (26, 28, 8),
                28: (27, 29, 15),
                29: (28, 30, 2),
                30: (29, 31, 25),
                31: (30, 0, 12),
            },
        )

    def test_PappusGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(
            LCFNotation([5, 7, -7, 7, -7, -5], 3),
            {
                0: (17, 1, 5),
                1: (0, 2, 8),
                2: (1, 3, 13),
                3: (2, 4, 10),
                4: (3, 5, 15),
                5: (4, 6, 0),
                6: (5, 7, 11),
                7: (6, 8, 14),
                8: (7, 9, 1),
                9: (8, 10, 16),
                10: (9, 11, 3),
                11: (10, 12, 6),
                12: (11, 13, 17),
                13: (12, 14, 2),
                14: (13, 15, 7),
                15: (14, 16, 4),
                16: (15, 17, 9),
                17: (16, 0, 12),
            },
        )

    def test_TutteCoxeterGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(
            LCFNotation([-13, -9, 7, -7, 9, 13], 5),
            {
                0: (29, 1, 17),
                1: (0, 2, 22),
                2: (1, 3, 9),
                3: (2, 4, 26),
                4: (3, 5, 13),
                5: (4, 6, 18),
                6: (5, 7, 23),
                7: (6, 8, 28),
                8: (7, 9, 15),
                9: (8, 10, 2),
                10: (9, 11, 19),
                11: (10, 12, 24),
                12: (11, 13, 29),
                13: (12, 14, 4),
                14: (13, 15, 21),
                15: (14, 16, 8),
                16: (15, 17, 25),
                17: (16, 18, 0),
                18: (17, 19, 5),
                19: (18, 20, 10),
                20: (19, 21, 27),
                21: (20, 22, 14),
                22: (21, 23, 1),
                23: (22, 24, 6),
                24: (23, 25, 11),
                25: (24, 26, 16),
                26: (25, 27, 3),
                27: (26, 28, 20),
                28: (27, 29, 7),
                29: (28, 0, 12),
            },
        )

    def test_GrayGraph(self):
        """ Check that the graph generation works."""
        # TODO actually test that it makes the correct graph.
        self.assertEqual(
            LCFNotation([-25, 7, -7, 13, -13, 25], 9),
            {
                0: (53, 1, 29),
                1: (0, 2, 8),
                2: (1, 3, 49),
                3: (2, 4, 16),
                4: (3, 5, 45),
                5: (4, 6, 30),
                6: (5, 7, 35),
                7: (6, 8, 14),
                8: (7, 9, 1),
                9: (8, 10, 22),
                10: (9, 11, 51),
                11: (10, 12, 36),
                12: (11, 13, 41),
                13: (12, 14, 20),
                14: (13, 15, 7),
                15: (14, 16, 28),
                16: (15, 17, 3),
                17: (16, 18, 42),
                18: (17, 19, 47),
                19: (18, 20, 26),
                20: (19, 21, 13),
                21: (20, 22, 34),
                22: (21, 23, 9),
                23: (22, 24, 48),
                24: (23, 25, 53),
                25: (24, 26, 32),
                26: (25, 27, 19),
                27: (26, 28, 40),
                28: (27, 29, 15),
                29: (28, 30, 0),
                30: (29, 31, 5),
                31: (30, 32, 38),
                32: (31, 33, 25),
                33: (32, 34, 46),
                34: (33, 35, 21),
                35: (34, 36, 6),
                36: (35, 37, 11),
                37: (36, 38, 44),
                38: (37, 39, 31),
                39: (38, 40, 52),
                40: (39, 41, 27),
                41: (40, 42, 12),
                42: (41, 43, 17),
                43: (42, 44, 50),
                44: (43, 45, 37),
                45: (44, 46, 4),
                46: (45, 47, 33),
                47: (46, 48, 18),
                48: (47, 49, 23),
                49: (48, 50, 2),
                50: (49, 51, 43),
                51: (50, 52, 10),
                52: (51, 53, 39),
                53: (52, 0, 24),
            },
        )

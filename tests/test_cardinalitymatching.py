from unittest import TestCase

from seqs.CardinalityMatchingAlt2 import matching, greedy_matching

# g = {0: {1: (0, 1), 2: (0, 2), 4: (0, 4)}, 1: {0: (1, 0), 3: (1, 3), 5: (1, 5)}, 2: {3: (2, 3), 0: (2, 0), 6: (2, 6)}, 3: {2: (3, 2), 1: (3, 1), 7: (3, 7)}, 4: {5: (4, 5), 6: (4, 6), 0: (4, 0)}, 5: {4: (5, 4), 7: (5, 7), 1: (5, 1)}, 6: {7: (6, 7), 4: (6, 4), 2: (6, 2)}, 7: {6: (7, 6), 5: (7, 5), 3: (7, 3)}}

g = {
    "A": ["B", "D", "I"],
    "B": ["A", "I", "C", "D"],
    "C": ["B",],
    "D": ["E", "F", "G", "H", "I", "A", "B"],
    "E": ["D",],
    "F": ["G", "D"],
    "G": ["D", "F"],
    "H": ["D",],
    "I": ["A", "B", "D",],
}

matching(g, initial_matching=None)

greedy_matching(g, initial_matching=None)

print("test")

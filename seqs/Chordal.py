"""Chordal.py

Recognize and compute elimination ordering of chordal graphs, using
an algorithm from Habib, McConnell, Paul, and Viennot, "Lex-BFS and
Partition Refinement, with Applications to Transitive Orientation,
Interval Graph Recognition, and Consecutive Ones Testing", Theor.
Comput. Sci. 234:59-84 (2000), http://www.cs.colostate.edu/~rmm/lexbfs.ps

D. Eppstein, November 2003.
"""

from seqs.Graphs import isUndirected

from seqs.LexBFS import LexBFS


def PerfectEliminationOrdering(G):
    """Return a perfect elimination ordering, or raise an exception if not chordal.
    G should be represented in such a way that "for v in G" loops through
    the vertices, and "G[v]" produces a list of the neighbors of v; for
    instance, G may be a dictionary mapping each vertex to its neighbor set.
    Running time is O(n+m) and additional space usage over G is O(n+m).
    """
    alreadyProcessed = set()
    B = list(LexBFS(G))
    position = {B[i]: i for i in range(len(B))}
    leftNeighbors = {}
    parent = {}
    for v in B:
        leftNeighbors[v] = set(G[v]) & alreadyProcessed
        alreadyProcessed.add(v)
        if leftNeighbors[v]:
            parent[v] = B[max([position[w] for w in leftNeighbors[v]])]
            if not leftNeighbors[v] - {parent[v]} <= leftNeighbors[parent[v]]:
                raise ValueError("Input to PerfectEliminationOrdering is not chordal")
    B.reverse()
    return B


def Chordal(G):
    """Test if a given graph is chordal."""
    if not isUndirected(G):
        raise ValueError("Input to Chordal is not an undirected graph")
    try:
        PerfectEliminationOrdering(G)
    except:
        return False
    return True

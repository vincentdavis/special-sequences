"""
Graphs.py

Various examples of small standard named graphs.

D. Eppstein, September 2005.

AND

Various simple functions for graph input.

Each function's input graph G should be represented in such a way that "for v in G" loops through the
vertices, and "G[v]" produces a list of the neighbors of v; for instance, G may be a dictionary mapping
each vertex to its neighbor set.

D. Eppstein, April 2004.
"""


def GeneralizedPetersenGraph(n, k):
    G = {}
    for i in range(n):
        G[i, True] = (i, False), ((i - 1) % n, True), ((i + 1) % n, True)
        G[i, False] = (i, True), ((i - k) % n, False), ((i + k) % n, False)
    return G


def GeneralizedCoxeterGraph(n, a, b):
    G = {}
    for i in range(n):
        G[i, 0] = (i, 1), (i, 2), (i, 3)
        G[i, 1] = (i, 0), ((i + 1) % n, 1), ((i - 1) % n, 1)
        G[i, 2] = (i, 0), ((i + a) % n, 2), ((i - a) % n, 2)
        G[i, 3] = (i, 0), ((i + b) % n, 1), ((i - b) % n, 1)
    return G


def CubeConnectedCycles(n):
    return {(x, y): [(x, (y + 1) % n), (x, (y - 1) % n), (x ^ (1 << y), y)]
            for x in range(1 << n) for y in range(n)}


def LCFNotation(L, n):
    """
    Construct the cubic Hamiltonian graph with LCF Notation L^n.
    See http://mathworld.wolfram.com/LCFNotation.html
    for a description of this notation.
    """
    n *= len(L)
    return {i: ((i - 1) % n, (i + 1) % n, (i + L[i % len(L)]) % n) for i in range(n)}


def isUndirected(G):
    """Check that G represents a simple undirected graph."""
    for v in G:
        if v in G[v]:
            return False
        for w in G[v]:
            if v not in G[w]:
                return False
    return True


def maxDegree(G):
    """Return the maximum vertex (out)degree of graph G."""
    return max([len(G[v]) for v in G])


def minDegree(G):
    """Return the minimum vertex (out)degree of graph G."""
    return min([len(G[v]) for v in G])


def copyGraph(G, adjacency_list_type=set):
    """
    Make a copy of a graph G and return the copy.
    Any information stored in edges G[v][w] is discarded.
    
    Most of the time, copy.deepcopy will be preferable to this function;
    however, unlike deepcopy, this function can change the data type
    of the adjacency list of the given graph.

    The second argument should be a callable that turns a sequence
    of neighbors into an appropriate representation of the adjacency list.
    Note that, while Set, list, and tuple are appropriate values for
    adjacency_list_type, dict is not -- use Util.map_to_constant instead.
    """
    return {v: adjacency_list_type(iter(G[v])) for v in G}


def InducedSubgraph(V, G, adjacency_list_type=set):
    """
    The subgraph consisting of all edges between pairs of vertices in V.
    """
    return {x: adjacency_list_type(y for y in G[x] if y in V)
            for x in G if x in V}


def union(*graphs):
    """Return a graph having all edges from the argument graphs."""
    out = {}
    for G in graphs:
        for v in G:
            out.setdefault(v, set()).update(list(G[v]))
    return out


def isIndependentSet(V, G):
    """
    True if V is an independent set of vertices in G, False otherwise.
    """

    class NonIndependent(Exception):
        pass

    def TestIndependent(seq):
        for x in seq:
            raise NonIndependent

    try:
        InducedSubgraph(V, G, TestIndependent)
        return True
    except NonIndependent:
        return False

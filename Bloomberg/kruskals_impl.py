class Graph:
    def __init__(self, V):
        self.V = V
        self.edges = []
        self.vertices = set()

    def addEdge(self, u, v, w):
        self.edges.append((u, v, w))
        self.vertices.add(u)
        self.vertices.add(v)

class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        parentA, parentB = self.find(a), self.find(b)
        if self.rank[parentA] < self.rank[parentB]:
            self.parent[parentA] = parentB
        else:
            self.parent[parentB] = parentA
            if self.rank[parentA] == self.rank[parentB]:
                self.rank[parentA] += 1

from collections import deque

def kruskalsMST(graph):
    unionFind = UnionFind(list(graph.vertices))

    edges = deque(sorted(graph.edges, key = lambda x : x[2]))
    res = []
    while len(res) < graph.V - 1:
        u, v, w = edges.popleft()
        uKey, vKey = unionFind.find(u), unionFind.find(v)
        if uKey != vKey:
            res += (u, v, w),
            unionFind.union(u, v)
    
    return res, sum([w for _, _, w in res])

if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
    res, cost = kruskalsMST(g)
    print("cost of MST from kruskal's {} and resultant edges {}".format(cost, res))
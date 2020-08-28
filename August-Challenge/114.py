class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        
    def union(self, a, b):
        aP = self.find(a)
        bP = self.find(b)
        
        if aP == bP:
            return False
        # optimize by rank
        if self.rank[aP] < self.rank[bP]:
            self.parent[aP] = bP
        else:
            self.parent[bP] = aP
            if self.rank[aP] == self.rank[bP]:
                self.rank[aP] += 1
                        
        return True
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # rules for valid tree
        # should have only one parent, all nodes connected
        # no cycles
        # union find
        if n-1 != len(edges):
            return False
        uf = UnionFind(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False
            
        return True
            
        
        
        
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
            
        
        
# Second attempt

class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}
    
    # union by rank
    def union(self,a,b) -> bool:
        # print("union of", a, b)
        parentA = self.find(a)
        parentB = self.find(b)
        if parentA == parentB:
            return False
        if self.rank[parentA] < self.rank[parentB]:
            self.parent[parentA] = parentB
        else:
            self.parent[parentB] = parentA
            if self.rank[parentA] == self.rank[parentB]:
                self.rank[parentA] += 1
        # print(self.parent, self.rank)
        return True
        
        
    # path compression
    def find(self,x):
        # print("calling find of",x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # write union and find class
        # also if e = n - 1 then false
        # if there is back edge then it's not a tree, so union helps in constructing tree
        # find helps in determining if its a valid tree
        if len(edges) != n-1:
            return False
        
        uf = UnionFind(n)
        for x, y in edges:
            if not uf.union(x, y):
                return False
        
        return True
        
        
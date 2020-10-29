class UnionFind:
    def __init__(self, capacity):
        self.parent = {i: i for i in range(capacity)}
        self.rank = {i: 0 for i in range(capacity)}

    def union(self, x, y):
        xKey = self.find(x)
        yKey = self.find(y)
        if self.rank[xKey] < self.rank[yKey]:
            self.parent[xKey] = yKey
        else:
            self.parent[yKey] = xKey
            if self.rank[xKey] = self.rank[yKey]:
                self.rank[xKey] += 1

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
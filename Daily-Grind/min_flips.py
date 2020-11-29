from collections import deque
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = sum(cell << (i * n + j) for i, row in enumerate(mat) for j, cell in enumerate(row))
        que = deque([(start, 0)])
        seen = {start}
        
        while que:
            node, steps = que.popleft()
            if not node:
                return steps
            for i in range(m):
                for j in range(n):
                    next = node
                    for r,c in [(i, j), (i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                        if m > r >= 0 <= c < n:
                            next ^= (1 << (r*n+c))
                    if next not in seen:
                        seen.add(next)
                        que += (next, steps+1),
                                
        return -1
        
        
        
        
        
        
        
        
        
        
        
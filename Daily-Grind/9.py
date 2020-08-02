from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        directions = [(0,1), (0,-1),(1,0), (-1,0)]
        
        m, n = len(grid), len(grid[0])
        que = deque([])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que += (i,j,0),
                    
        res = 0
        while que:
            x,y,_min = que.popleft()
            res = max(res, _min)
            for i,j in directions:
                nx, ny = x+i, y+j
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    que += (nx, ny, _min + 1),
                    grid[nx][ny] = 2
                            
        for row in grid:
            for orange in row:
                if orange == 1:
                    return -1
                
        return res
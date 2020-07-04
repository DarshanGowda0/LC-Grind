from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def bfs(i, j):
            que = deque([(i,j)])
            while que:
                x, y = que.popleft()
                for p, q in directions:
                    nx, ny = x + p, y + q
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '1':
                        que += (nx,ny),
                        visited[nx][ny] = True

        noOfIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    # start bfs
                    visited[i][j] = True
                    bfs(i, j)
                    noOfIslands += 1
                    
        return noOfIslands
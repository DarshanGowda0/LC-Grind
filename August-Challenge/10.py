from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use bfs with timestamp
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n = len(grid), len(grid[0])
        
        que = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i,j,0))
            
        maxTime = 0
        while que:
            # print(que)
            x, y, timestamp = que.popleft()
            maxTime = max(maxTime, timestamp)
            for i, j in directions:
                nx, ny = x+i, y+j
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                    que.append((nx,ny,timestamp+1))
                    grid[nx][ny] = 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
        return maxTime
                    
        
            
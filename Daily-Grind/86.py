class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # bfs should solve this
        
        if not grid or grid[0][0] == 1:
            return -1
        
        m,n = len(grid), len(grid[0])
        
        if grid[m-1][n-1] == 1:
            return -1
        
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        visited = set()
        
        que = collections.deque([(0,0,1)])
        visited.add((0,0))
        while que:
            x,y,dist = que.popleft()
            if (x,y) == (m-1,n-1):
                return dist
            for i, j in directions:
                nx, ny = x+i, y+j
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                    que += (nx,ny,dist+1),
                    visited.add((nx,ny))
                    
        return -1

    
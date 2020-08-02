class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        directions = [(0,1,1), (1,0, 2), (-1,0,3), (0,-1, 4)]
        m, n = len(grid), len(grid[0])
        
        def dfs(x,y,order, shape):
            shape.append(order)
            for i, j, p in directions:
                nx , ny = x+i, y+j
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited and grid[nx][ny]:
                    visited.add((nx,ny))
                    dfs(nx, ny, p, shape)
            shape.append(0)   
        
        
        visited = set()
        shapes = set()
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == 1:
                    shape = []
                    visited.add((i,j))
                    dfs(i,j,0, shape)
                    if shape:
                        shapes.add(tuple(shape))
        
        return len(shapes)
                        
        
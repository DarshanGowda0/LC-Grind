class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        # start from all nodes as starting nodes
        # do a greedy dfs with visited set
        # compare the gold obtained to max and update max
        # O(n^2)
        
        
        def dfs(grid, x, y, gold, visited):
            for p, q in directions:
                nx, ny = p+x, q+y
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] != 0:
                    # print("dfs {} => {}".format(grid[x][y], grid[nx][ny]))
                    visited.add((nx,ny))
                    gold += grid[nx][ny]
                    self.maxGold = max(gold, self.maxGold)
                    dfs(grid, nx, ny, gold, visited)
                    gold -= grid[nx][ny]
                    visited.remove((nx, ny))
                    
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.maxGold = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    # print('staring at ({},{})'.format(i,j))
                    visited = set()
                    visited.add((i,j))
                    self.maxGold = max(grid[i][j], self.maxGold)
                    dfs(grid, i, j, grid[i][j], visited)
                    
        return self.maxGold
                                
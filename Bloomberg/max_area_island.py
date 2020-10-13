class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # do dfs and mark visited as 0
        # return the val up and keep adding
        # compare the return val with global max
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1, 0), (0,-1)]
        
        def dfs(x, y):
            grid[x][y] = 0
            res = 1
            for p, q in directions:
                nx, ny = x+p, y+q
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    res += dfs(nx, ny)
            
            return res
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = dfs(i, j)
                    ans = max(ans, temp)
                    
        return ans
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # dp of choices
        
        def dfs(grid, i, j, k, dp={}):
            nonlocal m, n
            if i == m:
                return 0
            
            if (i, j, k) not in dp:
                gain = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if 0 <= j+x < n and 0 <= k+y < n:
                            curGain = grid[i][j+x] + grid[i][k+y] if j+x != k+y else grid[i][j+x]
                            nextGain = dfs(grid, i+1, j+x, k+y, dp)
                            gain = max(gain, curGain + nextGain)
                dp[(i, j, k)] = gain
            return dp[(i, j, k)]
        
        m, n = len(grid), len(grid[0])
        first = grid[0][0] + grid[0][n-1] if n-1 != 0 else grid[0][0]
        return first + dfs(grid, 1, 0, n-1)
                
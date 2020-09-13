class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # brute force is dfs along all paths
        # greedy approach to select only smallest among neighbors. might not work in edge cases
        m, n = len(grid), len(grid[0])
        def dfs(x,y,dp):
            if x == m or y == n:
                return float('inf')
            
            if x == m - 1 and y == n - 1:
                return grid[x][y]
            if (x,y) not in dp:
                dp[(x,y)] = grid[x][y] + min(dfs(x+1,y,dp), dfs(x, y+1, dp))
                
            return dp[(x,y)]
        
        dp = {}
        return dfs(0,0,dp)

# second attempt       
from collections import deque

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dfs with dp
        
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y, dp):
            if x >= m or y >= n:
                return float('inf')
            
            if (x,y) == (m-1, n-1):
                return grid[x][y]
            
            if (x,y) not in dp:
                dp[(x,y)] = grid[x][y] + min(dfs(x+1, y, dp), dfs(x, y+1, dp))
            
            return dp[(x,y)]
        
        return dfs(0,0,{})
                    
            
                    
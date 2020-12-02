class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # check if path is reachable
        # dp to the end, get the path chose and make all cells on path as zero
        # dp from end to top
        # dp[i][j] = grid[i][j] + max(dp[i][j-1], dp[i-1][j])
        """
        if not grid or grid[-1][-1] == -1:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        start = 0, 0
        que = collections.deque([start])
        reachable = False
        while que:
            x, y = que.popleft()
            if (x, y) == (m-1, n-1):
                reachable = True
                break
            for r, c in [(x+1, y), (x, y+1)]:
                if m > r >= 0 <= c < n and grid[r][c] != -1:
                    que += (r, c),
                    
        
        if not reachable:
            return 0
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]
        for i in reversed(range(m-1)):
            if grid[i][n-1] != -1:
                dp[i][n-1] = dp[i+1][n-1] + grid[i][n-1]
                
        for j in reversed(range(n-1)):
            if grid[m-1][j] != -1:
                dp[m-1][j] = dp[m-1][j+1] + grid[m-1][j]
        
        path = []
        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                if grid[i][j] != -1:
                    dp[i][j] = grid[i][j] + max(dp[i+1][j], dp[i][j+1])
                    
        def dfs(x, y):
            grid[x][y] = 0
            if x+1 >= m and y+1 >= n:
                return
            if x+1 >= m:
                dfs(x, y+1)
                return
            if y+1 >= n:
                dfs(x+1, y)
                return
            
            if dp[x+1][y] > dp[x][y+1]:
                dfs(x+1, y)
            else:
                dfs(x, y+1)

        # 0 to n-1
        res = dp[0][0]
        print(res)
        
        # make path as zero
        dfs(0,0)
        for row in grid:
            print(row)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            if grid[i][0] != -1:
                dp[i][0] = grid[i][0] + dp[i-1][0]
                
        for j in range(1, n):
            if grid[0][j] != -1:
                dp[0][j] = grid[0][j] + dp[0][j-1]
                
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])
                
        res += dp[-1][-1]
        
        return res
        """
        
        # dp with greedy wont work, one edge case 
        # [[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]
        N = len(grid)
        memo = [[[None for _ in range(N)] for _ in range(N)] for _ in range(N)]
        def dfs(r1, c1, c2):
            r2 = r1 + c1 - c2
            if (N == r1 or N == r2 or N == c1 or N == c2 or grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            
            if r1 == c1 == N-1:
                return grid[r1][c1]
            if memo[r1][c1][c2]:
                return memo[r1][c1][c2]
            
            ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
            ans += max(dfs(r1, c1+1, c2+1), dfs(r1+1, c1, c2+1), dfs(r1, c1+1, c2), dfs(r1+1, c1, c2))
            
            memo[r1][c1][c2] = ans
            return ans
        
        return max(0, dfs(0,0,0))
        
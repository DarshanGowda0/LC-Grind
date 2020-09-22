from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int, dp = {}) -> int:
        # do bfs and keep adding the coords on both directions
        # when you reach finsih, add the paths to res
        
        """TLE
        que = deque([(0,0,[])])
        res = []
        while que:
            x, y, path = que.popleft()    
            if (x, y) == (m-1, n-1):
                res += path,
            
            for p, q in [(1,0), (0,1)]:
                nx, ny = x+p, y+q
                if nx < m and ny < n:
                    que += (nx, ny, path[:]+[(x,y)]),
        # print(res)
        return len(res)
        """
        
        if m == 1 or n == 1:
            return 1
        if (m,n) not in dp:
            dp[(m,n)] = self.uniquePaths(m-1, n, dp) + self.uniquePaths(m,n-1, dp)
        
        return dp[(m,n)]

# second attempt

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp count number of ways at each decision if it leads to solution
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][n-1] = 1
        
        for j in range(n):
            dp[m-1][j] = 1
            
        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
                
        return dp[0][0]
                
                
        """
        def recur(x, y, dp):
            # print(x, y)
            if (x,y) == (m-1, n-1):
                return 1
            
            if x >= m or y >= n:
                return 0
            
            if (x,y) not in dp:
                count1 = recur(x+1, y, dp)
                count2 = recur(x, y+1, dp)

                dp[(x,y)] = count1 + count2
                
            return dp[(x,y)]
        
        return recur(0, 0, {})
        """
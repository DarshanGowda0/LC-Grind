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
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # eith dfs or bfs
        # every node with increasing nghbrs and visited set
        # bfs for every node with incr path
        # dfs with memoization
        
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dfs(x, y, visited, dp):
            # print(i, j)
            ans = 0
            for p, q in directions:
                nx, ny = p+x, q+y
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and matrix[nx][ny] > matrix[x][y]:
                    # print("visiting", (nx, ny))
                    if (nx, ny) not in dp:
                        visited.add((nx, ny))
                        dp[(nx, ny)] = dfs(nx, ny, visited, dp)
                        visited.remove((nx, ny))
                    ans = max(ans, dp[(nx, ny)])
            # print(ans)
            return 1 + ans
        
        res = 0
        dp = {}
        for i in range(m):
            for j in range(n):
                visited = {(i, j)}
                dp[(i, j)] = dfs(i, j, visited, dp)
                res = max(res, dp[(i, j)])
                
        return res
        
                     
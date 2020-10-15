class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # iterate and check how many nghbrs have 1
        # add all
        
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = 4
                    for p, q in directions:
                        nx, ny = i+p, j+q
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            temp -= 1
                    res += temp
                    
        return res
                            
                
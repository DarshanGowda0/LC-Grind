from collections import deque

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # bfs over all paths
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(grid), len(grid[0])
        start = None
        blocks = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    blocks += 1
                elif grid[i][j] == 1:
                    start = (i, j)    
                
        # position, pathSoFar, visited
        node = (start, [start], {start})
        que = deque([node])
        
        res = []
        while que:
            # print(que)
            position, pathSoFar, visited = que.popleft()
            if grid[position[0]][position[1]] == 2 and blocks == len(pathSoFar) - 2:
                res += pathSoFar,
                continue
            
            x, y = position
            for p, q in directions:
                nx, ny = p+x, q+y
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] != -1:
                    nVisited = set(visited)
                    nVisited.add((nx, ny))
                    node = ((nx, ny), pathSoFar + [(nx, ny)], nVisited)
                    que += node,
        
        return len(res)
    
    
### DFS 
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        non_obstacles = 0
        start_row, start_col = 0, 0
        for row in range(0, rows):
            for col in range(0, cols):
                cell = grid[row][col] 
                if  cell >= 0:
                    non_obstacles += 1
                if cell == 1:
                    start_row, start_col = row, col

        path_count = 0

        def backtrack(row, col, remain):
            nonlocal path_count

            if grid[row][col] == 2 and remain == 1:
                path_count += 1
                return

            temp = grid[row][col] 
            grid[row][col] = -4
            remain -= 1

            for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = row + ro, col + co

                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue
                if grid[next_row][next_col] < 0:
                    continue

                backtrack(next_row, next_col, remain)

            grid[row][col] = temp

        backtrack(start_row, start_col, non_obstacles)

        return path_count

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
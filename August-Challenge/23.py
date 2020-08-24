from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        #bfs 
        #every start node, go in all four directions untill you hit the wall
        #add the point at which you hit the wall into que
        m, n = len(maze), len(maze[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        que = deque([start])
        seen = {(start[0], start[1])}
        while que:
            # print(que)
            x, y = que.popleft()
            
            if [x,y] == destination:
                return True
            for p, q in directions:
                nx , ny = p+x, q+y
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                    nx, ny = nx+p, ny+q
                nx, ny = nx - p, ny - q
                if (nx, ny) not in seen:
                    que += (nx,ny),
                    seen.add((nx, ny))
                    
        return False
                    
        
            
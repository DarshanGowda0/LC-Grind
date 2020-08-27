from collections import deque

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # bfs on each node on all directions with <= val, mark flags on touching the borders
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ans = []
        for i in range(m):
            for j in range(n):
                seen = set()
                seen.add((i,j))
                que = deque([(i,j)])
                pacific, atlantic = False, False
                while que:
                    x, y = que.popleft()
                    for p, q in directions:
                        nx, ny = x+p, y+q
                        if 0 <= nx < m and 0 <= ny < n:
                            if matrix[nx][ny] <= matrix[x][y] and (nx,ny) not in seen:
                                que += (nx,ny),
                                seen.add((nx,ny))
                        elif nx < 0 or ny < 0:
                            pacific = True
                        elif nx >= m or ny >= n:
                            atlantic = True
                        
                    if pacific and atlantic:
                        ans += (i,j),
                        break
                
        
        return ans

                            
                            
                            
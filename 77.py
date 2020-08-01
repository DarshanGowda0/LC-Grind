from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if not image:
            return image
        
        color = image[sr][sc]
        if color == newColor:
            return image
        
        res = image[:]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m, n = len(image), len(image[0])
        que = deque([(sr, sc)])
        res[sr][sc] = newColor
        while que:
            x, y = que.popleft()
            
            for p, q in directions:
                nx, ny = x+p, y+q
                if 0 <= nx < m and 0 <= ny < n and res[nx][ny] == color:
                    res[nx][ny] = newColor
                    que.append((nx,ny))
                    
        return res
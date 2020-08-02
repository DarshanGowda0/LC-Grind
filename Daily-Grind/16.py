class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board or not board[0]:
            return False
        
        m,n = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def recur(x, y, word, visited):
            # print(x,y,word, visited)
            if not word:
                return True
            
            for i, j in directions:
                nx, ny = x+i, y+j
                if (nx,ny) not in visited and 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[0]:
                    visited.add((nx,ny))
                    ret = recur(nx, ny, word[1:], visited)
                    if ret:
                        return True
                    visited.remove((nx,ny))
                
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i,j))
                    ret = recur(i,j, word[1:], visited)
                    if ret:
                        return True
                    
        return False
        
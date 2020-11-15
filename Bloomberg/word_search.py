class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs with backtracking
        
        def dfs(x, y, idx, visited):
            if idx == len(word):
                return True
            nonlocal m, n, directions
            for p, q in directions:
                nx, ny = p+x, q+y
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and board[nx][ny] == word[idx]:
                    visited.add((nx, ny))
                    val = dfs(nx, ny, idx+1, visited)
                    if val:
                        return True
                    visited.remove((nx, ny))
            
            return False
                    
        
        m, n = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1, 0), (0,-1)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = {(i, j)}
                    if dfs(i, j, 1, visited):
                        return True
        
        return False
                    
            
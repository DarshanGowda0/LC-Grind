class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        isChanged = False
        
        for i in range(m):
            for j in range(n-2):
                if abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]) != 0:
                    board[i][j] = board[i][j+1] = board[i][j+2] = -abs(board[i][j])
                    isChanged = True
        
        for i in range(m-2):
            for j in range(n):
                if abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]) != 0:
                    board[i][j] = board[i+1][j] = board[i+2][j] = -abs(board[i][j])
                    isChanged = True
                    
        for c in range(n):
            l = m - 1
            for r in range(m - 1, -1, -1):
                if board[r][c] > 0:
                    board[l][c] = board[r][c]
                    l -= 1
                    
            for r in range(l, -1, -1):
                board[r][c] = 0
                
        return self.candyCrush(board) if isChanged else board
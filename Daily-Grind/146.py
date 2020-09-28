class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player
        n = len(self.board)
        # check row
        if all([cell == player for cell in self.board[row]]):
            return player
        
        # col
        for i in range(n):
            if self.board[i][col] != player:
                break
        else:
            return player
        
        #dia
        if row == col:
            for i in range(n):
                if self.board[i][i] != player:
                    break
            else:
                return player
            
            
        if row == (n - 1) - col:
            for i in range(n):
                if self.board[i][n-1-i] != player:
                    break
            else:
                return player
            
        return 0
        
        
    

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
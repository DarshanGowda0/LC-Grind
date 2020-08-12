class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # change to other numbers, assume -1 as dead and 2 as live from live
        # 3 as live from dead
        if not board or not board[0]:
            return 
        
        m, n = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        for i in range(m):
            for j in range(n):
                neigh = 0
                for x, y in directions:
                    nx, ny = i+x, y+j
                    
                    if 0 <= nx < m and 0 <= ny < n and (board[nx][ny] in {1, -1, 2}):
                        neigh += 1
                    # print("in",nx, ny, neigh)
                # print(i, j, neigh)
                # dead
                if board[i][j] == 0 and neigh == 3:
                    board[i][j] = 3
                elif board[i][j] == 1:
                    if neigh < 2 or neigh > 3:
                        board[i][j] = -1
                    else:
                        board[i][j] = 2
                        
        print(board)
                        
        for i in range(m):
            for j in range(n):
                if board[i][j] in {2, 3}:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0
        
        
                    
                    
        
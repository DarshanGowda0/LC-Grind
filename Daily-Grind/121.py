class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # dfs with backtracking, if found add to result
        # takes a long time
        # construct Trie for words and use trie node on grid traversal
        
        m, n = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        trie = {}
        for word in words:
            node = trie
            for l in word:
                if l not in node:
                    node[l] = {}
                node = node[l]
            node['$'] = word
        
        # print(trie)
        res = []
            
        def recur(x, y, node):
            c = board[x][y]
            cur = node[c]
            
            if '$' in cur:
                res.append(cur['$'])
                del cur['$']

            # visited
            board[x][y] = '#'
            
            for p, q in directions:
                nx, ny = p+x, q+y
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in cur:
                    recur(nx, ny, cur)
                    
            board[x][y] = c
            
            if not cur:
                del node[c]
                
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    recur(i, j, trie)
              
        return res
                

# second attempt

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct a trie for the words
        # start dfs with every node from the board and and cross off all words in the trie
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        res = []
        m, n = len(board), len(board[0])
        
        def dfs(i, j, node, seen):
            childNode = node[board[i][j]]
            if '$' in childNode:
                res.append(childNode['$'])
                del childNode['$']
                
            for p, q in directions:
                nx, ny = p+i, q+j
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in seen and board[nx][ny] in childNode:
                    seen.add((nx, ny))
                    dfs(nx, ny, childNode, seen)
                    seen.remove((nx,ny))
        
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = word
        
        
        
        for i in range(m):
            for j in range(n):
                node = trie
                if board[i][j] in node:
                    seen = {(i,j)}
                    dfs(i, j, node, seen)
                    # seen.remove((i,j))
                    
        return res
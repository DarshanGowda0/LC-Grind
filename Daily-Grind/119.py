class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans

#second attempt
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # define directions in order
        # perform dfs in the order of directions until you hit end
        if not len(matrix):
            return []
        m, n = len(matrix), len(matrix[0])
        
        
        di = [(0,1), (1,0), (0,-1), (-1,0)]
        
        seen = set()
        res = []
        i = 0
        x, y = 0, 0
        for _ in range(m*n):
            res += matrix[x][y],
            seen.add((x,y))
            nx, ny = x + di[i][0], y + di[i][1]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                x, y = nx, ny
            else:
                i = (i + 1) % 4
                x, y = x + di[i][0], y + di[i][1]
        
        return res
        
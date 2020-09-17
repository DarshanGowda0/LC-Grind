class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        if is_col:
            for i in range(R):
                matrix[i][0] = 0

# second attempt
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # set the flags on the top row/col
        # iterate all except top row & col
        # iterate again and make all corresponding rows and columns zero
        # iterate the top row and column to mark them zero
        
        isFirstCol = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                isFirstCol = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
                    
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
         
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0 
                
        if isFirstCol:        
            for i in range(len(matrix)):
                matrix[i][0] = 0
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # start from top-right or bottom-left
        # starting from top-right, if greater go down , else go left
        
        if not matrix:
            return False
        
        m,n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j > -1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i+=1
            else:
                j-=1
                
        return False
        
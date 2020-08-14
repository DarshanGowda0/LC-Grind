class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 1 0 0 0 0
        # 1 1 0 0 0
        # 1 2 1 0 0
        # 1 3 3 1 0
        # 1 4 6 4 1
        
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                res[j] = res[j] + res[j-1]
                
        return res
                
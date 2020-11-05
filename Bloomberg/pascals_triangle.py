class Solution:
    # 1
    # 1 1
    # 1 2 1
    # 1 3 3 1
    # 1 4 6 4 1
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range( numRows):
            temp = [1] * (i+1)
            for j in range(1, i):
                # print(i, j, res)
                temp[j] = res[i-1][j] + res[i-1][j-1]
            
            res += temp,
            
        return res
                
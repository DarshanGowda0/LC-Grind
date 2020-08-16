class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # []
        # [] [1]
        # [] [1] [2] [1,2]
        # [] [1] [2] [1,2], [3] [1,3] [2,3] [1,2,3]
        
        res = []
        res += [],
        for num in nums:
            n = len(res)
            for i in range(n):
                res += (res[i][:] + [num]),
                
        return res
from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # []
        # [1]
        # [1,2], [2,1]
        # [3,1,2], [1,3,2], [1,2,3], [3,2,1], [2,3,1], [2,1,3]
        
        res = [] # [3,2,1], [2,3,1], [2,1,3]
        que = deque([])
        que += [],
        
        for num in nums: #3
            n = len(que) # 2, [2,1] [1,2]
            for _ in range(n): # 2
                oldPerm = que.popleft() # [2,1]
                for i in range(len(oldPerm)+1): # 0,1,2
                    newPerm = oldPerm[:] # [2,1]
                    newPerm.insert(i, num) # 
                    if len(newPerm) == len(nums):
                        res += newPerm,
                    else:
                        que += newPerm, # []
                        
        return res
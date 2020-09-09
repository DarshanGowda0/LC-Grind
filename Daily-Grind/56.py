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

# Second attempt

from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # use bit manipulation
        # use bfs method 
        
        # BFS method
        # when len == 3: add to res
        # [] -> [1] -> [2,1] [1,2] -> [3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]
        
        que = deque([[]])
        res = []
        idx = 0
        while len(que):
            # print(que)
            for x in range(len(que)): # 1
                temp = que.popleft() # [1]
                # print("temp", temp)
                if len(temp) == len(nums):
                    res += temp,
                    break

                for i in range(len(temp)+1): # 2
                    newList = temp[:i] + [nums[idx]] + temp[i:]
                    # print(newList)
                    que += newList,

            idx+=1
        
        return res
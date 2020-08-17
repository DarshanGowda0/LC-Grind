from collections import deque

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        
        res = deque()
        res += [],
        
        for num in nums:
            n = len(res)
            for _ in range(n):
                perm = res.popleft()
                for i in range(len(perm)+1):
                    newPerm = perm[:]
                    newPerm.insert(i, num)
                    if len(newPerm) == len(nums):
                        ans.add(tuple(newPerm))
                    else:
                        res += newPerm,
                        
        return ans


li = []

li.append(10)

li += [10]





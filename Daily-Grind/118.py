class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        
        for num in numSet:
            if num - 1 not in numSet:
                cur = num
                streak = 1
                
                while cur+1 in numSet:
                    cur = cur+1
                    streak+=1
                
                ans = max(ans, streak)
                
        return ans
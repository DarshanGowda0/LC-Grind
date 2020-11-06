class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # sliding window technique
        
        start, end = 0, 0
        windowSum = 0
        res = float('inf')
        
        while end < len(nums):
            num = nums[end]
            windowSum += num
            
            while windowSum >= s:
                res = min(res, end - start + 1)
                windowSum -= nums[start]
                start += 1

            end += 1
        return res if res != float('inf') else 0
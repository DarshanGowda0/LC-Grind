class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        snums = sorted(nums)
        left, right = len(nums), 0
        for i in range(len(nums)):
            if snums[i] != nums[i]:
                left = min(left, i)
                right = max(right, i)
        
        
        return right - left + 1 if right - left >= 0 else 0
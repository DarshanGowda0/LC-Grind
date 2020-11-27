class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        nextSmaller = [len(nums)] * len(nums)
        stack = []
        
        for i, v in enumerate(nums):
            while stack and stack[-1][1] > v:
                nextSmaller[stack.pop()[0]] = i
            
            stack += (i, v),
            
        return sum([v - i for i, v in enumerate(nextSmaller)])
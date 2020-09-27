class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        snums = sorted(nums)
        left, right = len(nums), 0
        for i in range(len(nums)):
            if snums[i] != nums[i]:
                left = min(left, i)
                right = max(right, i)
        
        
        return right - left + 1 if right - left >= 0 else 0

# second attempt

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # brute force - n2 solution
        # take number at i and scan i:n, if you find a number less than at i, then thats start
        # same from other end
        
        # sorting is much better, n logn
        
        # use stack to find left most and right most unsorted
        
        stack = []
        l, r = len(nums), 0
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
            
        stack.clear()
        
        for i in reversed(range(len(nums))):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(stack.pop(), r)
            stack.append(i)
        
        return r - l + 1 if r - l > 0 else 0
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor operator
        ans = 0
        for i in range(len(nums)):
            ans ^= (i+1)
            ans ^= nums[i]
            
        return ans
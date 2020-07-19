class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i+=1
            j+=1
        
        
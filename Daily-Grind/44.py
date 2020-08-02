class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        for idx in range(len(nums)):
            # print(idx, nums)
            if nums[abs(nums[idx])-1] > 0:
                nums[abs(nums[idx])-1] *= -1
        
        print(nums)
        
        res = [idx+1 for idx in range(len(nums)) if nums[idx] > 0]
        
        return res
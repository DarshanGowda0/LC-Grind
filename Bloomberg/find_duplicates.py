class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res = []
        
        for num in nums:
            nums[abs(num)-1] *= -1
            
        for num in nums:
            if nums[abs(num)-1] > 0:
                res += abs(num),
                nums[abs(num)-1] *= -1
                
        return res
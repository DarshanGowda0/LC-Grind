class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = 0
        count = 0
        
        for num in nums:
            if count == 0:
                n = num
            if n == num:
                count += 1
            else:
                count -= 1
                
        return n
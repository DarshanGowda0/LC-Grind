class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # can't use sliding window since the numbers can be -ve
        # most naive is try all combinations of subarrays - O(n^3)
        
        """
        TLE 
        k = 1
        pro = float('-inf')
        while k <= len(nums):
            for i in range(len(nums)-k+1):
                temp = 1
                for j in range(i, i+k):
                    temp *= nums[j]
                pro = max(pro, temp)
            k+=1
        
        return pro
        """
        
        if not nums:
            return 0
        
        res, minSoFar, maxSoFar = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            cur = nums[i]
            temp = max(cur, maxSoFar * cur, minSoFar * cur)
            minSoFar = min(cur, maxSoFar * cur, minSoFar * cur)
            
            maxSoFar = temp
            res = max(res, maxSoFar)
            
        return res

# second attempt

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxSoFar = nums[0]
        minSoFar = nums[0]
        res = maxSoFar
        
        for num in nums[1:]:
            tempMax = max(num, maxSoFar*num, minSoFar*num)
            minSoFar = min(num, maxSoFar*num, minSoFar*num)
            maxSoFar = tempMax
            
            res = max(res, maxSoFar)
            
        return res
            
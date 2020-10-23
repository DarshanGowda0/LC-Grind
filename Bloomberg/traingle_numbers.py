class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # select three nums such that a + b > c
        # naive approach n^3
        # optimize -> sort and binary search
        # sort and use k as boundary
        
        count = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            k = i+2
            if nums[i] == 0:
                continue
            for j in range(i+1,n-1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k+=1
                count += k - j - 1
                
        
        return count
                
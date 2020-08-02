class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def recur(first=0):
            if first == n:
                res.append(nums[:])
                
            for idx in range(first,n):
                
                nums[idx], nums[first] = nums[first], nums[idx]
                recur(first+1)
                nums[idx], nums[first] = nums[first], nums[idx]
            

        n = len(nums)
        res = []
        recur()
        return res
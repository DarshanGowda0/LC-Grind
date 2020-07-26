class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def recur(nums):
            if not nums:
                return 
            ans.add(tuple(nums[:]))
            for i in range(len(nums)):
                recur(nums[:i] + nums[i+1:])
            
        ans = set()
        recur(nums)
        ans.add(tuple([]))
        return ans
        
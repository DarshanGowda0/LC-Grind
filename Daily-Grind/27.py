class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(nums, idx, dp):
            if idx >= len(nums):
                return 0
            
            if idx not in dp:
                robCurrent = nums[idx] + dfs(nums, idx+2, dp)
                skipCurrent = dfs(nums, idx+1, dp)
                dp[idx] = max(robCurrent, skipCurrent)
            
            return dp[idx]
        
        dp = {}
        return dfs(nums, 0, dp)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(nums, idx, prev, dp):
            
            if idx >= len(nums):
                return 0
            
            include = 0
            
            # key = "{}-{}".format(idx, prev)
            
            if dp[idx][prev] == -1:
                if prev == -1 or nums[idx] > nums[prev]:
                    include = 1 + dfs(nums, idx+1, idx, dp)

                skip = dfs(nums, idx+1, prev, dp)

                dp[idx][prev] = max(include, skip)
        
            return dp[idx][prev]
        
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
        return dfs(nums, 0, -1, dp)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob or skip a house and check all combinations,
        # if rob , then skip adjacent
        # include last if you skip first
        
        def recur(nums, idx, dp):
            if idx >= len(nums):
                return 0
            
            if (idx, len(nums)) not in dp:
                rob = nums[idx] + recur(nums[:-1] if idx == 0 else nums, idx+2, dp)
                skip = recur(nums, idx+1, dp)

                dp[idx, len(nums)] = max(rob, skip)
            return dp[(idx, len(nums))]
        
        dp = {}
        return recur(nums, 0, dp)
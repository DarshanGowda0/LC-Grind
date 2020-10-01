class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find one subset with sum = sum(all) / 2
        
        def dfs(nums, idx, _sum, dp):
            # print(idx, _sum)
            if _sum == 0:
                # print("returning")
                return True
            
            if idx >= len(nums):
                return False
            
            key = (_sum, idx)
            
            if key not in dp:
                
                # include
                if nums[idx] <= _sum:
                    if dfs(nums, idx+1, _sum - nums[idx], dp):
                        dp[key] = True
                        return True
                # skip
                dp[key] = dfs(nums, idx+1, _sum, dp)
                
            return dp[key]
            
            
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        
        return dfs(nums, 0, _sum // 2, {})
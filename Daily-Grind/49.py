class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
    
        def dfs(nums, idx, _sum, dp):
            
            if _sum == 0 and idx == len(nums):
                return 1
            
            if idx >= len(nums):
                return 0            

            key = (idx, _sum)
            if key not in dp:
                count1 = dfs(nums, idx+1, _sum + nums[idx], dp)
                count2 = dfs(nums, idx+1, _sum - nums[idx], dp)

                dp[key] = count1 + count2
            return dp[key]

        
        dp = {}
        return dfs(nums, 0, S, dp)
            
        
        
# second attempt
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # try all cominations
        # if any of the two operations lead to target at the end, then return 1
        
        def dfs(nums, idx, target, soFar, dp):
            if idx == len(nums):
                return 1 if soFar == target else 0
            
            key = (idx, soFar)
            if key not in dp:
                # addition
                c1 = dfs(nums, idx+1, target, soFar+nums[idx], dp)
                # subtration
                c2 = dfs(nums, idx+1, target, soFar-nums[idx], dp)
                
                dp[key] = c1+c2
            return dp[key]
        
        dp = {}
        return dfs(nums, 0, S, 0, dp)
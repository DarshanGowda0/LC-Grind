class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(coins, idx, amount, dp):
            
            if amount == 0:
                return 0
            
            if idx >= len(coins):
                return float('inf')
            
            key = "{}-{}".format(idx, amount)
            
            if key not in dp:
                include = float('inf')
                if coins[idx] <= amount:
                    temp = dfs(coins, idx, amount - coins[idx], dp)
                    if temp != float('inf'):
                        include = 1 + temp

                skip = dfs(coins, idx+1, amount, dp)

                dp[key] = min(include, skip)
                
            return dp[key]
        
        dp = {}
        ans = dfs(coins, 0, amount, dp)
        return ans if ans != float('inf') else -1
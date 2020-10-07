class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # use unbounded knapsack technique
        
        """
        def dfs(coins, idx, amount, dp):
            
            if amount == 0:
                return 0
            
            if idx >= len(coins):
                return float(inf)
            
            if (idx, amount) not in dp:
                c1 = float('inf')
                if coins[idx] <= amount:
                    val = dfs(coins, idx, amount - coins[idx], dp)
                    if val != float('inf'):
                        c1 = 1 + val

                c2 = dfs(coins, idx+1, amount, dp)

                dp[(idx, amount)] = min(c1, c2)
            
            return dp[(idx, amount)]
        
        ans = dfs(coins, 0, amount, {})
        return ans if ans != float('inf') else -1
        """
        
        # bottom-up iterative
        
        dp = [[float(inf) for _ in range(amount+1)] for _ in range(len(coins))]
        
        # when amount = 0
        for i in range(len(coins)):
            dp[i][0] = 0
        
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    dp[i][j] = (1 + dp[i][j - coins[i]]) if dp[i][j - coins[i]] != float('inf') else float('inf')
                    
                dp[i][j] = min(dp[i][j], dp[i-1][j])
                
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
                    
    
        
            
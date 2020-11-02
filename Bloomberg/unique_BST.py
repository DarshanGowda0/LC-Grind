class Solution:
    def numTrees(self, n: int) -> int:
        # from educative subsets pattern
        
        def recur(n, dp):
            # trees with just 1/0 node
            if n <= 1:
                return 1
            
            if n in dp:
                return dp[n]
            
            count = 0
            for i in range(1, n+1):
                countOfLeftTrees = recur(i-1, dp)
                countOfRightTrees = recur(n - i, dp)
                count += (countOfLeftTrees * countOfRightTrees)
                
            dp[n] = count
            return dp[n]
                
        return recur(n, {})
            
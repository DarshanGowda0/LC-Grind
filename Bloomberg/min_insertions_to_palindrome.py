class Solution:
    def minInsertions(self, s: str) -> int:
        # find lps and return len(s) - len(lps) 
        # longest palindromic subsequence
        """
        def recur(s, idx1, idx2, dp):
            if idx1 > idx2:
                return 0
            
            if idx1 == idx2:
                return 1
            
            key = (idx1, idx2)
            
            if key not in dp:
            
                if s[idx1] == s[idx2]:
                    return 2 + recur(s, idx1 + 1, idx2 - 1, dp)

                l1 = recur(s, idx1 + 1, idx2, dp)
                l2 = recur(s, idx1, idx2 - 1, dp)

                dp[key] = max(l1, l2)
                
            return dp[key]
        
        lps = recur(s, 0, len(s) - 1, {})
        """
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            
        for i in range(len(s) - 2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        lps = dp[0][len(s)-1]
        
        # print(lps)
        return len(s) - lps
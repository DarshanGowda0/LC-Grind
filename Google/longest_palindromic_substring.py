class Solution:
    def longestPalindrome(self, s: str) -> str:
        # bottom up dp
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        res = None
        
        for i in range(n):
            dp[i][i] = True
            res = s[i]
            
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res = s[i:i+2]
           
        for k in range(2, n+1):
            for i in range(n-k):
                j = i+k
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res = s[i:j+1]
                    
        return res
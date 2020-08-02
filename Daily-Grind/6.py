class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        lStr = ""
        for i in range(len(s)):
            dp[i][i] = True
            lStr = s[i]
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                lStr = s[i:i+2]
        
        for k in range(2, len(s)):
            for i in range(len(s)-k):
                j = i + k
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    lStr = s[i:j+1]
        
        return lStr
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        def recur(idx, dp):
            
            if idx == len(s):
                return 1
            
            if s[idx] == '0':
                return 0
            
            if idx == len(s) - 1:
                return 1
            
            if idx not in dp:
                s1 = 0
                if int(s[idx: idx+2]) <= 26:
                    s1 = recur(idx+2, dp)
                
                s2 = recur(idx+1, dp)
                
                dp[idx] = s1+s2
                
            return dp[idx]
        
        return recur(0, {})
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def recur(word1, word2, idx1, idx2, dp={}):
            m, n = len(word1), len(word2)
            if idx1 == m:
                return n - idx2
            
            if idx2 == n:
                return m - idx1
            
            key = (idx1, idx2)
            
            if key not in dp:
            
                if word1[idx1] == word2[idx2]:
                    return recur(word1, word2, idx1+1, idx2+1, dp)

                c1 = 1 + recur(word1, word2, idx1, idx2+1, dp)
                c2 = 1 + recur(word1, word2, idx1+1, idx2, dp)
                c3 = 1 + recur(word1, word2, idx1+1, idx2+1, dp)

                dp[key] = min(c1, c2, c3)
            return dp[key]
        
        return recur(word1, word2, 0, 0)
        
        
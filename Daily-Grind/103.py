class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # compare individual chars from both strings in increasing order
        # return the max of all such comparisons
        # memoize the dfs solution
        
        def dfs(idx1, idx2, dp):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            
            _key = (idx1,idx2)
            if _key not in dp:
            
                #include
                include = 0
                if text1[idx1] == text2[idx2]:
                    include = 1 + dfs(idx1+1, idx2+1 ,dp)

                skip1 = dfs(idx1+1, idx2, dp)
                skip2 = dfs(idx1, idx2+1, dp)
                
                dp[_key] =  max(include, skip1, skip2)
            
            return dp[_key]
        
        dp = {}
        return dfs(0, 0, dp)
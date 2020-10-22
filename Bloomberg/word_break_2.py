from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
            
        def dfs(string, wordSet, dp):
            if not string:
                return [[]]
            
            if string in dp:
                return dp[string]
            
            for idx in range(len(string)):
                soFar = string[:idx+1]
                if soFar in wordSet:
                    for sentence in dfs(string[idx+1:], wordSet, dp):
                        dp[string] += [soFar] + sentence,
                
                
            return dp[string]
                
        dp = defaultdict(list)
        dfs(s, set(wordDict), dp)
        
        return [" ".join(words) for words in dp[s]]
                
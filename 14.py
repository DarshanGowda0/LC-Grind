class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mSet = set(wordDict)
        
        def recur(word, dp={}):
            if word == "":
                return True
            
            if word in dp:
                return dp[word]
            
            for i in range(len(word)):
                if word[:i+1] in mSet:
                    ret = recur(word[i+1:], dp)
                    dp[word[i+1:]] = ret
                    if ret:
                        return True
            
            return False
        
        return recur(s, {})
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # sort dict by validity and score
        # then use 0/1 dp to get max score/ could be greedy as well?
        
        def dfs(fWords, letterCount, idx, dp = {}):
            if idx == len(fWords):
                return 0
            
            key = (idx, tuple(letterCount.items()))
            # print(key)
            if key not in dp:
                score1 = 0
                # include
                word, profit, wordC = fWords[idx]
                letterC = dict(letterCount)
                for k, v in wordC.items():
                    if k not in letterC or v > letterC[k]:
                        break
                    else:
                        letterC[k] -= wordC[k]
                        if not letterC[k]:
                            del letterC[k]
                else:
                    # print("including word", word, letterC)
                    score1 = profit + dfs(fWords, letterC, idx+1, dp)
                
                # skip
                score2 = dfs(fWords, letterCount, idx+1, dp)
                
                dp[key] = max(score1, score2)
                
            return dp[key]
            
        
        letterCount = Counter(letters)
        filteredWords = []
        for word in words:
            wordCounter = Counter(word)
            for k, val in wordCounter.items():
                if k not in letterCount or val > letterCount[k]:
                    break
            else:
                filteredWords += (word, sum([score[ord(c) - ord('a')] for c in word]), wordCounter),
        # print(filteredWords)
        return dfs(filteredWords, letterCount, 0)
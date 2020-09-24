from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        tDict = Counter(t)
        
        l, r = 0, 0
        required = len(tDict)
        
        formed = 0
        
        windowDict = defaultdict(int)
        n = len(s)
        
        ans = float('inf'), 0, 0
        
        while r < n:
            char = s[r]
            
            windowDict[char] += 1
            if char in tDict and windowDict[char] == tDict[char]:
                formed += 1
            
            
            while l <= r and required == formed:
                if r - l + 1 < ans[0]:
                    ans = r-l+1, l, r
                
                char = s[l]
                windowDict[char]-=1
                if char in tDict and windowDict[char] < tDict[char]:
                    formed -= 1
                    
                l+=1
                     
            r += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
                
# second attempt
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep dictionary of T and numberOfUniqueChars 
        # use sliding window and determine the min window
        
        tDict = {}
        for c in t:
            if c not in tDict:
                tDict[c] = 0
            tDict[c]+=1
        
        uniqueChars = len(tDict)
        
        start, end = 0, 0
        
        sDict = {}
        found = 0
        res = float('inf')
        out = ""
        while end < len(s):
            # print("end", end, "start", start)
            char = s[end]
            if char not in sDict:
                sDict[char] = 0
            sDict[char]+=1
            
            if char in tDict and sDict[char] == tDict[char]:
                found+=1
                if found == uniqueChars and end - start + 1 < res:
                    res = end - start + 1
                    out = s[start:end+1]
                    
            # try and decrease the window by increasing start
            if found == uniqueChars:
                while start <= end and found == uniqueChars:
                    # print("start", start)
                    if end - start + 1 < res:
                        res = end - start + 1
                        out = s[start:end+1]

                    char = s[start]
                    sDict[char] -= 1
                    if char in tDict and sDict[char] < tDict[char]:
                        found -= 1
                    start += 1                
                        
            
            end += 1
        
        return out
        
        
        
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
                
                
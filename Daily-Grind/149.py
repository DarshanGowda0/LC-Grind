from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #maintain a sliding window dict of len p
        #if all freq match, take start
        
        pDict = Counter(p)
        start = 0
        found = 0
        res = []
        
        for end in range(len(s)):
            char = s[end]
            if char in pDict:
                pDict[char] -= 1
                if pDict[char] == 0:
                    found += 1
            
            if found == len(pDict):
                res += start,
                
            if end >= len(p) - 1:
                char = s[start]
                start += 1
                if char in pDict:
                    if pDict[char] == 0:
                        found -= 1
                    pDict[char] += 1
            
        return res
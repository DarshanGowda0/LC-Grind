class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i, j = 0, 0
        mSet = {}
        l = 0
        
        while j < len(s):
            if s[j] in mSet:
                i = max(i, mSet[s[j]])
                
            l = max(l, j - i+1)
            mSet[s[j]] = j+1
            j += 1
            
        return l
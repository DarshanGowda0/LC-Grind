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

# second attempt
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain a window as map with indices
        # scan and add to window, if repeated then remove all the chars till last found idx from window
        
        windowMap = {}
        start, end = 0, 0
        n = len(s)
        ans = 0
        while end < n:
            # print(windowMap, start, end)
            char = s[end]
            if char in windowMap:
                idx = windowMap[char]
                while start <= idx:
                    del windowMap[s[start]]
                    start += 1
            
            windowMap[char] = end
            ans = max(ans, len(windowMap))
            end += 1
            
        return ans
            
        
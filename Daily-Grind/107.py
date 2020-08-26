class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # A A B A B B A
        #[A A B A] - 4
        # A A B[A B B A]
        
        if not s:
            return 0
        
        max_window_len = 1
        windowStart = 0
        charFrequency = {s[0]:1}
        maxChar = s[0]
        
        for i in range(1,len(s)):
            # print(charFrequency, windowStart, i)
            windowEnd = i
            if s[i] not in charFrequency:
                charFrequency[s[i]] = 0    
            charFrequency[s[i]] += 1
            
            if charFrequency[s[i]] > charFrequency[maxChar]:
                maxChar = s[i]
                
            if windowEnd - windowStart + 1 > charFrequency[maxChar] + k:
                charFrequency[s[windowStart]] -= 1
                windowStart += 1
                
            max_window_len = max(max_window_len, windowEnd - windowStart + 1)
        
        return max_window_len
                
                
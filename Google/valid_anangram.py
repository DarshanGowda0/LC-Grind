class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # counter technique
        counter = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
            
        for i in range(26):
            if counter[i] != 0:
                return False
            
        return True
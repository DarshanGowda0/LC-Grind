class Solution:
    def titleToNumber(self, s: str) -> int:
        
        
        i = 0
        res = 0
        for c in reversed(s):
            res += ((ord(c) - ord('A') + 1) * (26**i) )
            i+=1
        
        return res
        
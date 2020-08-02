class Solution:
    def countSubstrings(self, s: str) -> int:
        
        tab = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        count = 0
        for i in range(len(s)):
            tab[i][i] = True
            count += 1
            
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                tab[i-1][i] = True
                count += 1
            
        for k in range(3, len(s) + 1):
            for i in range(len(s) - k + 1):
                j = i + k - 1
                if s[i] == s[j] and tab[i+1][j-1]:
                    count += 1
                    tab[i][j] = True
                    
        return count
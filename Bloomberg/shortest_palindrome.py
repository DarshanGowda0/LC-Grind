class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        # find longest palindromic substring from idx 0
        # add rev of s[p:] to front and return
        # a a c e c a a a
        # 0 1 2 3 4 5 6 7
        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
                
            return True
        
        P = 0
        for j in range(len(s) - 1, -1, -1):
            if isPalindrome(s, 0, j):
                P = j + 1
                break
                
        
        return s[P:][::-1] + s
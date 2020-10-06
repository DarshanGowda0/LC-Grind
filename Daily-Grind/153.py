class Solution:
    def validPalindrome(self, s: str) -> bool:
        # find the longest palidrome sbsequence and then return len(lps) - l(s) == 1
        """
        def dfs(s, idx1, idx2, dp):
            
            if idx1 == idx2:
                return 1
            
            if idx1 > idx2:
                return 0

            if (idx1, idx2) not in dp:
            
                if s[idx1] == s[idx2]:
                    dp[(idx1, idx2)] = 2 + dfs(s, idx1+1, idx2-1, dp)
                    return dp[(idx1, idx2)]


                c1 = dfs(s, idx1+1, idx2, dp)
                c2 = dfs(s, idx1, idx2-1, dp)
                
                dp[(idx1, idx2)] = max(c1, c2)
            
            return dp[(idx1, idx2)]
        
        val = dfs(s, 0, len(s)-1, {})

        return len(s) - val <= 1
        TLE
        """
        
        def isPalindrome(s, low, high):
            while low <= high:
                if s[low] != s[high]:
                    return False
                low+=1
                high-=1
                
            return True
        
        low, high = 0, len(s)-1
        
        while low < high:
            if s[low] == s[high]:
                low+=1
                high-=1
            else:
                return isPalindrome(s, low+1, high) or isPalindrome(s, low, high-1)
        
        return True
            
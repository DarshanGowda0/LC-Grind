class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def recur(l, r, n, s, res):
            if l < n:
                recur(l+1,r,n,s+'(', res)
            if r < l:
                recur(l, r+1, n, s+')', res)
            elif l == r == n:
                res += s,
        
        res = []
        recur(0,0,n,"", res)
        return res
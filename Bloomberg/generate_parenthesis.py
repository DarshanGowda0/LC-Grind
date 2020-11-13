class Parenthesis:
    def __init__(self, open=0, close=0, string=""):
        self.open = open
        self.close = close
        self.string = string
        
    def __str__(self):
        return self.string

from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
        que = deque([Parenthesis()])
        res = []
        while que:
            p = que.popleft()
            if p.open == n and p.close == n:
                res += p.string,
                continue
                
            if p.open < n:
                que += Parenthesis(p.open+1, p.close, p.string + "("),
            
            if p.close < p.open:
                que += Parenthesis(p.open, p.close + 1, p.string + ")"), 
                
        return res
                
            
        
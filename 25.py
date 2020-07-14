class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for idx, val in enumerate(s):
            if val in ('(',')'):
                if stack and stack[-1][1] == '(' and val == ')':
                    stack.pop()
                else:
                    stack += (idx, val),
                    
        S = [c for c in s]
        print(stack)
        while stack:
            idx, _  = stack.pop()
            S.pop(idx)

        return "".join(S)
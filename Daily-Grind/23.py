class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if stack and ((c == '}' and stack[-1] == '{') or (c == ']' and stack[-1] == '[') or (c == ')' and stack[-1] == '(')):
                    stack.pop()
            else:
                stack += c,
                
        return not stack
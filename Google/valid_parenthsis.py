class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mDict = {')':'(', ']': '[', '}':'{'}
        for c in s:
            if stack and (c in mDict and mDict[c] == stack[-1]):
                stack.pop()
            else:
                stack += c,
                
        return len(stack) == 0
        
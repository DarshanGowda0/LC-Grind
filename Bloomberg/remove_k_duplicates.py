class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            # print(c)
            if not stack or stack[-1][0] != c:
                stack += (c, 1),
            else:
                stack[-1] = (c, stack[-1][1] + 1)
                if stack[-1][1] == k:
                    stack.pop()
            # print(stack)    
        return "".join([c*i for c,i in stack])
                
        
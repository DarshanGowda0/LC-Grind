class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        
        res = [0] * len(T)
        for idx, temp in enumerate(T):
            while stack and stack[-1][1] < temp:
                i, _ = stack.pop()
                res[i] = idx - i
            stack += (idx, temp),
            
        return res
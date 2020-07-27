class Solution:
    def fib(self, N: int) -> int:
        
        if N == 0 or N == 1:
            return N
        
        arr = [0] * (N + 1)
        
        arr[0], arr[1] = 0, 1
        
        for i in range(2, N+1):
            arr[i] = arr[i-1] + arr[i-2]
            
        return arr[-1]
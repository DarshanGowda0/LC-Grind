from collections import deque

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s)
        arr = deque([i for i in range(1, n+2)])
        res = [0] * (n+1)
        que = deque()
        for idx, c in enumerate(s):
            if c == 'I':
                que += idx,
                
        while que:
            idx = que.popleft()
            res[idx] = arr.popleft()
            idx -= 1
            while idx > -1 and res[idx] == 0:
                res[idx] = arr.popleft()
                idx -= 1
            
        # print(arr)
        idx = len(res) - 1
        while idx > -1 and res[idx] == 0:
            res[idx] = arr.popleft()
            idx -= 1
        return res
            
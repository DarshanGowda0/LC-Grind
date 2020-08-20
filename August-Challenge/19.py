from collections import deque

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # naive is to build all combinations of k 
        
        if N == 0:
            return 0
        
        if N == 1:
            return [(i+K) % 10 for i in range(10)]
        
        seen = set()
        
        que = deque()
        for i in range(1,10):
            que.append(i)
            
        while que:
            # print(que)
            num = que.popleft()
            
            if len(str(num)) == N:
                seen.add(num)
                continue
            lastDigit = num % 10
            if lastDigit == K:
                newNum = num * 10 
                que += newNum,
            if lastDigit + K < 10:
                newNum = (num * 10) + lastDigit + K
                que += newNum,
            if lastDigit - K > -1:
                num = (num * 10) + lastDigit - K
                que += num,
            
        return list(seen)
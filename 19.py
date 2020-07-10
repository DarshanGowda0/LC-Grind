from heapq import *

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        
        res = 0
        while len(sticks) > 1:
            x, y = heappop(sticks), heappop(sticks)
            res += (x + y)
            heappush(sticks, x+y)
        
        return res
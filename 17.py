from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = [(y**2 + x**2, x, y) for x, y in points]
        heapify(heap)
        
        res = []
        
        for _ in range(K):
            _, x, y = heappop(heap)
            res += [x,y],
        
        return res
                
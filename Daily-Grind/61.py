from collections import defaultdict
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mMap = defaultdict(int)
        for num in nums:
            mMap[num] += 1
        
        heap = []
        for key, val in mMap.items():
            if len(heap) < k:
                heappush(heap, (val, key))
            elif val > heap[0][0]:
                heappushpop(heap, (val, key))
               
        # print(heap)
        ans = [val for _, val in heap]
        
        return ans
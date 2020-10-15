from collections import defaultdict

from heapq import *

class Solution:
    def frequencySort(self, s: str) -> str:
        # n log n solutions
        # count chars, and sort by chars
        # count chars, heapify and pop one by one
        
        cMap = defaultdict(int)
        for c in s:
            cMap[c] += 1
            
        # return "".join(sorted(s, key = lambda x: -cMap[x]))
    
        heap = [(-count, char) for char, count in cMap.items()]
        heapify(heap)
        res = []
        while heap:
            count, c = heappop(heap)
            count *= -1
            # print(count)
            for _ in range(count):
                res += c,
            
        return "".join(res)
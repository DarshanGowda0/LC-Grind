from heapq import *
from collections import deque

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        intervals.sort()
        que = deque(intervals)
        s, e = que.popleft()
        heap = [[e,s]]
        
        while que:
            end, start = heap[0]
            tStart, tEnd = que.popleft()
            if tStart < end:
                heappush(heap, [tEnd, tStart])
            else:
                heapreplace(heap, [tEnd, tStart])
        return len(heap)
                
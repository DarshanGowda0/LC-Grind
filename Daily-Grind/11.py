from queue import PriorityQueue
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        
        que = PriorityQueue()
        
        for interval in intervals:
            que.put(interval)
        
        res = []
        start, end = que.get()
        while not que.empty():
            tStart, tEnd = que.get()
            if end >= tStart:
                end = max(end, tEnd)
            else:
                res.append([start,end])
                start, end = tStart, tEnd
                
        res.append([start,end])
                
        return res
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # heapify and insert and then just merge
        # or anyway sorted so just insert and merge one - going with this
        # cases - start time overlap with prev interval
        # end time overlap with next interval
        # interval overlaps with both prev and next
        # interval overlaps within one interval
        # [1, 3] [6, 9]
        # [2, 5]
        # [1, ]
        start, end = newInterval
        
        idx, n = 0, len(intervals)
        res = []
        
        # add all intervals before the overlap to result
        while idx < n and intervals[idx][0] < start:
            res += intervals[idx],
            idx += 1
            
        if not res or res[-1][1] < start:
            res += [start, end],
        else:
            res[-1][1] = max(res[-1][1], end)
            
        while idx < n:
            s, e = intervals[idx]
            if res[-1][1] < s:
                res += [s, e],
            else:
                res[-1][1] = max(res[-1][1], e)
            idx += 1
        
        return res
            
        
        
            
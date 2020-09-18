class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        sList = sorted(intervals)
        prev = sList[0][1]
        ans = 0
        print(sList)
        for start, end in sList[1:]:
            if start < prev:
                ans += 1
                prev = min(prev, end)
            else:
                prev = end
        
        return ans

# second attempt
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy approach
        # sort by starting times, remove the one with greater end time if conflict occurs
        
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[0])
        ans = 0
        end = intervals[0][1]
        for s, e in intervals[1:]:
            if s < end:
                ans += 1
                end = min(end, e)
            else:
                end = e
        
        return ans
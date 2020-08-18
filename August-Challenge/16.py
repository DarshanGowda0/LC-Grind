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
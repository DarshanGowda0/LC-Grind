class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort meetings by start time
        # if any endTimes overlap with next startTime then false, else true
        if not intervals:
            return True
        intervals.sort()
        endTime = intervals[0][1]
        for start, end in intervals[1:]:
            if start < endTime:
                return False
            endTime = end
            
        return True
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class EmployeeInterval:
    def __init__(self, interval, employeeIdx, intervalIdx):
        self.interval = interval
        self.employeeIdx = employeeIdx
        self.intervalIdx = intervalIdx
        
    def __lt__(self, other):
        return self.interval.start < other.interval.start
    
    def __eq__(self, other):
        return self.interval.start == otherInterval.start
    
    def __str__(self):
        return "({},{}) - {} - {}".format(self.interval.start, self.interval.end, self.employeeIdx, self.intervalIdx)

from heapq import *
    
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        minHeap = []
        
        for idx in range(len(schedule)):
            heappush(minHeap, EmployeeInterval(schedule[idx][0], idx, 0))
            
        prev = minHeap[0]
        
        res = []
        
        while minHeap:
            curInterval = heappop(minHeap)
            # print(curInterval)
            if curInterval.interval.start > prev.interval.end:
                res += Interval(prev.interval.end, curInterval.interval.start),
                
            remainingList = schedule[curInterval.employeeIdx]
            if curInterval.intervalIdx + 1 < len(remainingList):
                heappush(minHeap, EmployeeInterval(schedule[curInterval.employeeIdx][curInterval.intervalIdx+1], curInterval.employeeIdx, curInterval.intervalIdx + 1))
                
            if prev.interval.end < curInterval.interval.end:
                prev = curInterval
            
        return res
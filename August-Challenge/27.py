from collections import deque

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = 0
        last7, last30 = deque(), deque()
        
        for day in days:
            while last7 and last7[0][0] + 7 <= day:
                last7.popleft()
            while last30 and last30[0][0] + 30 <= day:
                last30.popleft()
            
            last7 += (day, cost + costs[1]),
            last30 += (day, cost + costs[2]),
            
            cost = min(cost + costs[0], last7[0][1], last30[0][1])
            
        return cost
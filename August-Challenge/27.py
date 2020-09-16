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

# second attempt
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        def dfs(days, idx, nxt, costs, dp):
            while idx < len(days) and days[idx] < nxt:
                idx+=1
            
            if idx >= len(days):
                return 0
				
            key = (idx, nxt)
            if key not in dp:
                day1 = costs[0] + dfs(days, idx+1, days[idx]+1, costs, dp)
                day7 = costs[1] + dfs(days, idx+1, days[idx]+7, costs, dp)
                day30 = costs[2] + dfs(days, idx+1, days[idx]+30, costs, dp)

                val = min(day1, day7, day30)
                dp[key] = val
            return dp[key]
        
        return dfs(days, 0, 0, costs, {})
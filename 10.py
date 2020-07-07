class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        _min = prices[0]
        ans = float('-inf')
        
        for day in prices[1:]:
            _min = min(_min, day)
            ans = max(ans, (day - _min))
            
        return ans if ans > 0 else 0
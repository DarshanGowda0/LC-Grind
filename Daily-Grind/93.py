class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > m:
                profit += (prices[i] - m)
            m = prices[i]
            
        return profit
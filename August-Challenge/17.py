class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not n:
            return 0
        leftArr, rightArr = [0] * n, [0] * n
        
        minLeft = prices[0]
        for i in range(1, n):
            leftArr[i] = max(leftArr[i-1],prices[i] - minLeft)
            minLeft = min(minLeft, prices[i])
            
        maxRight = prices[-1]
        for i in range(n-2, -1, -1):
            rightArr[i] = max(maxRight - prices[i], rightArr[i+1])
            maxRight = max(maxRight, prices[i])
            
        maxProfit = 0
        for i in range(n):
            profit = leftArr[i] + rightArr[i]
            maxProfit = max(maxProfit, profit)
            
        return maxProfit
        
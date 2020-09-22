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
        

# second attempt

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """x
        # profit from making one transaction
        def profit(prices):
            if not prices:
                return 0
            _min = prices[0]
            ans = 0
            for price in prices[1:]:
                ans = max(ans, price - _min)
                _min = min(_min, price)
                
            return ans
        
        res = 0
        for i in range(len(prices)):
            tempAns = profit(prices[:i]) + profit(prices[i:])
            res = max(res, tempAns)
            
        return res
        """
        
        if not prices:
            return 0
        
        leftProfits = [0] * len(prices)
        rightProfits = [0] * len(prices)
        
        lowest = prices[0]
        for i in range(1, len(prices)):
            leftProfits[i] = max(leftProfits[i-1], prices[i] - lowest)
            lowest = min(lowest, prices[i])
        
        
        highest = prices[-1]
        for i in reversed(range(len(prices) - 1)):
            rightProfits[i] = max(rightProfits[i+1], highest - prices[i])
            highest = max(highest, prices[i])
        
        ans = rightProfits[0]
        for i in range(1, len(prices)):
            ans = max(ans, leftProfits[i-1] + rightProfits[i])
            
        return ans
        
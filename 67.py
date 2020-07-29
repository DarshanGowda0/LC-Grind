from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        def sumOfDigits(num):
            ans = 0
            while num:
                q, r = divmod(num, 10)
                ans += r
                num = q
            
            return ans
        
        mDict = defaultdict(int)
        largest = float('-inf')
        for i in range(1, n+1):
            tempSum = sumOfDigits(i)
            # print("sum of {} is {}".format(i, tempSum))
            mDict[tempSum] += 1
            largest = max(largest, mDict[tempSum])
            
        # print(mDict, largest)
        res = 0
        for _, val in mDict.items():
            if val == largest:
                res += 1
            
        return res
        
            
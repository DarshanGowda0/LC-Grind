from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cumSum = 0
        mDict = defaultdict(int)
        mDict[0] = 1
        
        for num in nums:
            cumSum += num
            if cumSum - k in mDict:
                count += mDict[cumSum -k]
            
            mDict[cumSum] += 1
            
        return count


# second attempt

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        if not nums:
            return 0
        
        preSum = [0 for _ in range(len(nums)+1)]
        preSum[0] = 0
        res = 0
        for i in range(1,len(nums)+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        
        # print(preSum)
        for start in range(0, len(nums)):
            for end in range(start+1, len(nums)+1):
                # print(end, start)
                if preSum[end] - preSum[start] == k:
                    res += 1
        
        return res
        """
        
        # using dict for cumilative Sum
        # sum -> numberOfSumOccurences
        preSum = defaultdict(int)
        preSum[0] = 1
        ans = 0
        sum = 0
        
        for num in nums:
            sum+=num
            ans += preSum[sum-k]
            preSum[sum] += 1
            
        return ans
            
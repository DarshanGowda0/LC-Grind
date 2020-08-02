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
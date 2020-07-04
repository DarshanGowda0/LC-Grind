class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mSet = {}
        for idx, n in enumerate(nums):
            diff = target-n
            if diff in mSet:
                return [mSet[diff], idx]
            mSet[n] = idx
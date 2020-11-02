class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        end = 0
        subsets = [[]]
        for idx, num in enumerate(nums):
            start = 0
            if idx > 0 and nums[idx] == nums[idx-1]:
                start = end + 1
            end = len(subsets) - 1
            for i in range(start, end+1):
                subsets += subsets[i] + [num],
        return subsets
            
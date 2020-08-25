class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def recur(nums, target, idx, path):
            if target == 0:
                ans.append(tuple(path))
                
            if idx >= len(nums) or target < 0:
                return 
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                recur(nums, target-nums[i], i+1, path+[nums[i]])
            
        candidates.sort()
        recur(candidates, target, 0, [])
        return ans
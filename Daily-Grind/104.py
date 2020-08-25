class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # naive solution
        # at every idx, either pick a number if its less than target or skip a number
        # if you pick a number add it to list and send it down the recursion
        # if sum reaches 0, add the list to soln
        
        
        ans = []
        def recur(candidates, target, listSoFar, idx):
            
            if target == 0:
                ans.append(tuple(listSoFar))
            
            if idx >= len(candidates) or target < 0:
                return 
            
            for i in range(idx, len(candidates)):
                recur(candidates, target - candidates[i], listSoFar + [candidates[i]], i)            
        recur(candidates, target, [], 0)
        
        return ans
            
            
            
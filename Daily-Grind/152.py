from collections import deque

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # process elements in que with weight
        
        que = deque([(val, 1) for val in nestedList])
        ans = 0
        while que:
            val, weight = que.popleft()
            if val.isInteger():
                ans += weight*val.getInteger()
            else:
                que += [(child, weight+1) for child in val.getList()]
        
        return ans
        
        
        
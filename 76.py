from collections import defaultdict

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        mDict = defaultdict(list)
        for idx, val in enumerate(S):
            mDict[val] += idx,
            
        res = []
        start, end = -1, -1
        for idx, val in enumerate(S):
            lastIdx = mDict[val][-1]
            end = max(end, lastIdx)
            if idx == end:
                res += (end-start),
                start = end
            
        return res
            
            
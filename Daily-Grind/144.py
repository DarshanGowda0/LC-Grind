from collections import defaultdict
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        allSeq = defaultdict(int)
        """
        def dfs(webList, idx, seq):
            # print(webList, seq)
            if len(seq) == 3:
                allSeq[tuple(seq)] += 1
                return
            
            if idx >= len(webList):
                return
            
            # include
            dfs(webList, idx+1, seq + [webList[idx]])
            
            # skip
            dfs(webList, idx+1, seq)
            
        """ 
        user2Web = defaultdict(list)
        
        for _, user, web in sorted(zip(timestamp, username, website)):
            user2Web[user] += web,
            
        for _, webList in user2Web.items():
            # print(webList)
            combs = set(combinations(webList, 3))
            for comb in combs:
                allSeq[comb] += 1
            
        return sorted(allSeq, key = lambda x : (-allSeq[x], x))[0]
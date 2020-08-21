from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # create an adj list
        
        # do dfs and explore all nodes
        # add to seen 
        # count number of starting nodes
        
        adjList = defaultdict(list)
        for p, q in edges:
            adjList[p] += q,
            adjList[q] += p,
            
        ans = 0
        seen = set()
        
        def dfs(node):
            if node not in adjList:
                return
            
            for neighbor in adjList[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        for i in range(n):
            if i not in seen:
                seen.add(i)
                ans += 1
                dfs(i)
                
        return ans
            
        
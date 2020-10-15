from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # JFK - SFO, ATL
        # SFO - ATL
        # ATL - JFK, SFO
        # JFK - ATL - JFK - SFO - ATL - SFO 
        
        # construct a adjList in sorted order
        # start from JFK as source and add to res and take a dfs walk untill all nodes are visited
        # if it reaches an end and all nodes are not visited, then backtrack
        adjList = defaultdict(list)
        
        for src, dst in tickets:
            adjList[src] += dst,
        
        
        visited = {}
        for src, val in adjList.items():
            val.sort()
            visited[src] = [False] * len(val)
        
        def dfs(node, pathSoFar):
            # print(node, pathSoFar)
            if len(pathSoFar) == len(tickets) + 1:
                return True, pathSoFar
            
            for idx, child in enumerate(adjList[node]):
                if not visited[node][idx]:
                    visited[node][idx] = True
                    r, p = dfs(child, pathSoFar + [child])
                    if r:
                        return r, p
                    visited[node][idx] = False
            
            return False, pathSoFar
            
        src = "JFK"
        r, p = dfs(src, [src])
        return p
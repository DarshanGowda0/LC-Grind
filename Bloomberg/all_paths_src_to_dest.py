from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # bfs from src to dstntn
        # piggy back all the nodes in a list
        
        que = deque([(0, [0])])
        dest = len(graph) - 1
        
        res = []
        while que:
            node, path = que.popleft()
            if node == dest:
                res += path,
                continue
                
            for child in graph[node]:
                que += (child, path + [child]),
            
            
        return res
            
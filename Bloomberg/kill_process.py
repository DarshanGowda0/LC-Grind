from collections import defaultdict, deque

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # maintain adjList of parent to children and do a bfs
        adjList = defaultdict(list)
        for pid, ppid in zip(pid, ppid):
            adjList[ppid] += pid,
            
        que = deque([kill])
        res = []
        while que:
            node = que.popleft()
            res += node,
            
            for child in adjList[node]:
                que += child,
                
        return res
        
            
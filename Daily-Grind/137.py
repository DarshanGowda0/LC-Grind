from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # w -> e
        # e -> r
        # r > t
        # t > f
        
        # construct adjList looping from top to bottom
        # do topological sort after that
        
        adjList = defaultdict(set)
        
        i, n = 0, len(words)
        indegree = {c: 0 for word in words for c in word }
        
        while i < n-1:
            first, second = words[i], words[i+1]
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    adjList[first[j]].add(second[j])
                    break
            else:
                if len(second) < len(first):
                    return ""
            
            i+=1
        
        
        
        for key, children in adjList.items():
            for node in children:
                indegree[node] += 1
        
        que = deque()
        for key, val in indegree.items():
            if not val:
                que += key,
        # print(adjList)
        
        res = []
        while que:
            # print(que, indegree)
            node = que.popleft()
            res += node,
            for child in adjList[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que += child,
        # print(indegree)          
        return "".join(res) if len(res) == len(indegree) else ""
                
                    
        
        
            
        
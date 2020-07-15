from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            adjList[course] += pre,
            indegree[pre] += 1
        
        visited = set()    
        que = deque()
        
        for idx in range(len(indegree)):
            # print(idx, indegree[idx])
            if indegree[idx] == 0:
                que.append(idx)
                visited.add(idx)
        # print(indegree,que)
        res = []
        while que:
            course = que.popleft()
            res += course,
            for node in adjList[course]:
                indegree[node] -= 1
                if node not in visited and indegree[node] == 0:
                    que.append(node)
                    visited.add(node)
       
        # print(res)
        return len(res) == numCourses
                    
            
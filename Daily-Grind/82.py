class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0 <- 1
        
        # construct adjList
        # use kahn's algo of 0 indegree
        
        adjList = collections.defaultdict(list)
        indegree = [0] * numCourses
        
        for pre, cou in prerequisites:
            adjList[cou] += pre,
            indegree[pre] += 1
            
        # print(adjList, indegree)
        
        que = collections.deque()
        # visited = set()
        for idx, val in enumerate(indegree):
            if val == 0:
                que.append(idx)
                # visited.add(idx)
        # print(que)
        
        res = []
        while que:
            cou = que.popleft()
            res.append(cou)
            for nbr in adjList[cou]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    que.append(nbr)
                    
        return res if len(res) == numCourses else []
            
                
        
        
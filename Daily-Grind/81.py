class Solution:
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
         # construct an adjacency list with the dictionary
        adjList = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                _key = word[:i] + "*" + word[i+1:]
                adjList[_key] += word,
        
        # perform bfs
        
        que = deque([(beginWord,[beginWord])]) # que has (word, [visitedListTillNow])
        res = []
        visited = {beginWord:1} #maintain a visited dictionary with visit time
        
        while len(que) > 0:
            word, _list = que.popleft()
            dist = len(_list) #distance from beginWord
            
            if word == endWord: #if found, add to result
                res += _list,
                continue
                
            for i in range(len(word)):
                _key = word[:i] + "*" + word[i+1:]
                for child in adjList[_key]:
                    # if the node is already visited in a previos timestamp, ignore it
                    if child not in visited or dist <= visited[child]:
                        que += (child,_list[:]+[child]),
                        visited[child] = dist
                        
        return res
        
        # perform DFS and backtrack to find a path, if found add to res
        
        """
        res = []
        self.shortest = float('inf')
        def dfs(word, visited, path):
            if word == endWord:
                res.append(path)
                self.shortest = min(self.shortest, len(path))
                return
            for i in range(len(word)):
                _key = word[:i] + "*" + word[i+1:]
                for child in adjList[_key]:
                    if child not in visited:
                        visited.add(child)
                        dfs(child, visited, path[:] + [child])
                        visited.remove(child)
                        
                       
        visited = {beginWord}
        dfs(beginWord, visited, [beginWord])
        return [path for path in res if len(path) == self.shortest ]
        """           
    
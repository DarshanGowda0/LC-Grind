from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # construct an adjacency list with the dictionary
        adjList = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                _key = word[:i] + "*" + word[i+1:]
                adjList[_key] += word,
        
        # perform bfs to find the shortest path
        
        visited = set()
        que = deque([(beginWord,1)])
        visited.add(beginWord)
        
        while que:
            word, dist = que.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                _key = word[:i] + "*" + word[i+1:]
                for child in adjList[_key]:
                    if child not in visited:
                        que += (child,dist+1),
                        visited.add(child)
                        
                        
        return 0
        
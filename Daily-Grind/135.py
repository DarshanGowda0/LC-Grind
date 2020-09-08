"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # use a hashmap and traverse the tree using bfs
        # at every visit add the clone node to map if not exists
        # traverse again and attach clone nodes to corresponding nodes
        if not node:
            return None
        
        mDict = {}
        que = deque([node])
        mDict[node] = Node(node.val)
        
        while que:
            treeNode = que.popleft()
            
            for child in treeNode.neighbors:
                if child not in mDict:
                    mDict[child] = Node(child.val)
                    que += child,
                mDict[treeNode].neighbors.append(mDict[child])

        return mDict[node]
            
        
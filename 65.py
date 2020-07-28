"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        # bfs from root, add to que
        # at each interval process those in que and create new list, add to result
        
        que = deque([root])
        res = []
        
        while que:
            tempQue = deque()
            tempRes = []
            for _ in range(len(que)):
                node = que.popleft()
                tempRes += node.val,
                for child in node.children:
                    tempQue.append(child)
            que = tempQue
            res += tempRes,
            
        return res

        
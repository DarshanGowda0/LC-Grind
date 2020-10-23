"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # do level order traversal 
        # traverse through nodes and attach next to right
        
        if not root:
            return root
        
        que = deque([root])
        levels = []
        while que:
            level = []
            for _ in range(len(que)):
                node = que.popleft()
                level.append(node)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            levels.append(level)
            
        for row in levels:
            prev = None
            while row:
                node = row.pop()
                node.next = prev
                prev = node
        
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # visit all the leaves, if on left add to result
        sum = 0
        if not root:
            return sum
        que = deque([(root, False)])
        while que:
            node,isLeft = que.popleft()
            if not node.left and not node.right:
                sum += node.val if isLeft else 0
            
            if node.left:
                que += (node.left, True),
            if node.right:
                que += (node.right, False),
        
        return sum
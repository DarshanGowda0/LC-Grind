# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root:
                return 0, root
            
            lDepth, lNode = dfs(root.left)
            rDepth, rNode = dfs(root.right)
            
            if lDepth > rDepth:
                return lDepth + 1, lNode
            if rDepth > lDepth:
                return rDepth + 1, rNode
            
            return lDepth + 1, root
        
        return dfs(root)[1]
        
        
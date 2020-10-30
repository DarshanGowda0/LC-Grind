# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        def recur(node):
            if not node:
                return []
            return  [node.val] + recur(node.left) + recur(node.right)
        
        return recur(root)
        """
        
        # iterative
        if not root:
            return []
        stack = []
        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            res += node.val,
            
            if node.right:
                stack += node.right,
            
            if node.left:
                stack += node.left,
        
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        def recur(node):
            if not node:
                return []
            return recur(node.left) + recur(node.right) + [node.val]
        
        return recur(root)
        """
        
        # iterative
        stack = []
        res = []
        
        while root or stack:
            while root:
                if root.right:
                    stack += root.right,
                stack += root,
                root = root.left
                
            root = stack.pop()
            
            if stack and stack[-1] == root.right:
                stack[-1] = root
                root = root.right
            else:
                res += root.val,
                root = None
                
        
        return res
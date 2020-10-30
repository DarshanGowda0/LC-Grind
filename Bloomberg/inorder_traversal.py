# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        def recur(node):
            if not node:
                return []
            return recur(node.left) + [node.val] + recur(node.right)
        
        return recur(root)
        """
        
        #iterative
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res += cur.val,
            
            cur = cur.right
            
        return res
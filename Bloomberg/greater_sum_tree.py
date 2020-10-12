# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # maintain a global val, that keeps accumulating
        # traverse right - node - left
        
        sumSoFar = 0
        
        def dfs(node: TreeNode):
            if not node:
                return node
            nonlocal sumSoFar
            
            node.right = dfs(node.right)
            sumSoFar += node.val
            node.val = sumSoFar
            node.left = dfs(node.left)
            
            return node
        
        return dfs(root)
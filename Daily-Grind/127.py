# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        maxPath = float('-inf')
        
        def recur(node):
            if not node:
                return 0
            
            nonlocal maxPath
            
            leftGain = max(recur(node.left), 0)
            rightGain = max(recur(node.right), 0)
            
            maxPath = max(maxPath, node.val + leftGain + rightGain)
            
            return node.val + max(leftGain, rightGain)
        
        recur(root)
        
        return maxPath
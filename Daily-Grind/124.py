# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, node: TreeNode) -> bool:
        # define left and right
        # at every recur if node is between left and right true
        # change left and right when recur down
        
        def recur(node, left, right):
            if not node:
                return True
            
            if node.val >= right or node.val <= left:
                return False
            
            return recur(node.left, left, node.val) and recur(node.right, node.val, right)
        
        return recur(node, float('-inf'), float('inf'))
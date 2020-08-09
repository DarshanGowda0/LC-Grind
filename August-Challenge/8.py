# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.closest = (float('inf'), None)
        
        def dfs(node):
            if not node:
                return
            
            temp = abs(node.val - target)
            if temp < self.closest[0]:
                self.closest = (temp, node.val)
            
            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)
                
        dfs(root)
        return self.closest[1]
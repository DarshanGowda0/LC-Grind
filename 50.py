# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def dfs(node, _sum):
            if not node:
                return
            
            if node.val == _sum:
                self.count += 1
                
            dfs(node.left, _sum - node.val)
            dfs(node.right, _sum - node.val)
        
        def path(root, sum):
            if not root:
                return 0
            dfs(root, sum)
            path(root.left, sum)
            path(root.right, sum)    
        
        self.count = 0
        path(root, sum)
        return self.count
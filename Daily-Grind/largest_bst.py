# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node:
                return 0, float('inf'), float('-inf')
            
            lN, lMin, lMax = dfs(node.left)
            rN, rMin, rMax = dfs(node.right)
            
            if lMax < node.val < rMin:
                return lN + rN + 1, min(node.val, lMin), max(node.val, rMax)
            
            return max(lN, rN), float("-inf"), float("inf")
            
        return dfs(root)[0]
                
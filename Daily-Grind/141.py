# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        # do dfs and at every node, return sum, num of nodes
        # compare with global max at every level
        
        maxAvg = float('-inf')
        
        def dfs(node: TreeNode):
            if not node:
                return (0, 0)
            
            nonlocal maxAvg
            
            leftSum, leftNodes = dfs(node.left)
            rightSum, rightNodes = dfs(node.right)
            
            curAvg = (leftSum + rightSum + node.val) / (leftNodes + rightNodes + 1)
            # print(node.val, leftSum, rightSum, leftNodes, rightNodes)
            maxAvg = max(maxAvg, curAvg)
            
            return (leftSum + rightSum + node.val, leftNodes + rightNodes + 1)
        
        dfs(root)
        return maxAvg
            
            
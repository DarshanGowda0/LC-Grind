# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def dfs(prev, node, dp):
            
            if not node:
                return 0
            
            include = 0
            key = (prev, node)
            if key not in dp:
                print(node.val)
                if prev.left != node and prev.right != node:
                    include = node.val + dfs(node, node.left, dp) + dfs(node, node.right, dp)

                skip = dfs(prev, node.left, dp) + dfs(prev, node.right, dp)

                dp[key] = max(include, skip)
            
            return dp[key]
        
        dp = {}
        return dfs(TreeNode(), root, dp)
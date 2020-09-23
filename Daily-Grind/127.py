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

# second attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # take left path sum and right pathsum + val compareto global
        # return max(left, right) to parent
        
        ans = float('-inf')
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            nonlocal ans
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            
            ans = max(ans, node.val + left + right)
            
            return node.val + max(left, right)
        
        dfs(root)
        return ans
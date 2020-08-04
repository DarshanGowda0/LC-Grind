# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        self.sum = 0
        def dfs(root):
            if not root:
                return
            # print('visiting {}'.format(root.val))
            if L <= root.val <= R:
                self.sum += root.val
                
            if L < root.val:
                dfs(root.left)
            if R >= root.val:
                dfs(root.right)
        
        dfs(root)
        return self.sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        # brute force is to build inorder traversal => sorted array, return arr[k - 1]
        # we can do better, since it's BST
        
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        res = []
        inorder(root)
        return res[k-1]
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
#         def inorder(root):
#             if not root:
#                 return 
#             inorder(root.left)
#             ans.append(root.val)
#             inorder(root.right)
        
#         ans = []
#         inorder(root)
#         return ans

        stack = []
        cur = root
        ans = []
        while stack or cur:

            while cur:
                stack += cur,
                cur = cur.left

            node = stack.pop()
            ans += node.val,
            if node.right:
                cur = node.right


        return ans
        
        
        
        

        
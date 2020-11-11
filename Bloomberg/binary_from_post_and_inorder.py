# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def recur(left, right):
            if left > right:
                return None
            
            val = postorder.pop()
            node = TreeNode(val)
            
            i = idx[val]
            node.right = recur(i+1, right)
            node.left = recur(left, i-1)
            
            return node
        
        idx = {val:i for i, val in enumerate(inorder)}
        return recur(0, len(inorder)-1)
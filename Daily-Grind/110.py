# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # make inorder traversal and store in string, check if t is substring of s
        # use recursion comparing every node of s with root of t
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        def recur(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            
            return s.val == t.val and recur(s.left, t.left) and recur(s.right, t.right)
        
        return recur(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def mirror(root):
            if not root:
                return None
            
            left = mirror(root.right)
            right = mirror(root.left)
            
            return TreeNode(root.val, left, right)
        
        def compareTrees(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            return node1.val == node2.val and compareTrees(node1.left, node2.left) and compareTrees(node1.right, node2.right)
            
        mirrorTree = mirror(root)
        return compareTrees(root, mirrorTree)
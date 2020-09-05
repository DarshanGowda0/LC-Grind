# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # process nodes in preorder order, as root nodes to be attached next
        # group nodes in inorder as left subtree and right subtree
        
        inorderMap = {val:idx for idx, val in enumerate(inorder)}
        que = deque(preorder)
        
        def recur(start, end):
            if start > end:
                return None
            
            val = que.popleft()
            idx = inorderMap[val]
            node = TreeNode(val)
            node.left = recur(start, idx-1)
            node.right = recur(idx+1, end)
            
            return node
        
        return recur(0, len(preorder) - 1)
            
            
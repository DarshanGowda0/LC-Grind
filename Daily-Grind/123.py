# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # postorder and search
        # find p and q recursively and build parent map
        # from q start visiting anscesotrs one by one until one exists in p
        
        def find(node, parent):
            if not node:
                return
            if node.left:
                parent[node.left] = node
                find(node.left, parent)
            if node.right:
                parent[node.right] = node
                find(node.right, parent)
        
        parent = {root: None}
        find(root, parent)
        
        p_parents = {p.val}
        node = p
        while node:
            node = parent[node]
            if node:
                p_parents.add(node.val)
        # print(p_parents)
        node = q
        while node:
            if node.val in p_parents:
                return node
            node = parent[node]
        
        return None
        
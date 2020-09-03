# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # consider the root as lca
        # at every recur call, if p <= node <= q, then thats one of ans
        # else if node <= p, go right and if node >= q go left 
        self.low = root
        
        def recur(node, p, q):
            if not node:
                return 
            # print(node.val)
            
            self.low = node
            # print(node.val , p.val, q.val)
            if p.val < node.val and q.val < node.val:
                recur(node.left, p, q)
            elif p.val > node.val and q.val > node.val:
                recur(node.right, p, q)
                
        recur(root, p , q)
        return self.low
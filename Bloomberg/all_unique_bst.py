# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        # from educative subsets 
        def recur(start, end):
            if start > end:
                return [None]
            
            res = []
            for i in range(start, end + 1):
                left = recur(start, i-1)
                right = recur(i+1, end)
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left, node.right = l, r
                        res += node,
                        
            return res
        
        if n <= 0:
            return []
        return recur(1, n)
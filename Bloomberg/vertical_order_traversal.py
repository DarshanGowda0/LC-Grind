# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        table = defaultdict(list)
        que = deque([(root, 0)])
        minCol = maxCol = 0
        
        while que:
            node, col = que.popleft()
            
            if node:
                table[col].append(node.val)
                
                minCol = min(minCol, col)
                maxCol = max(maxCol, col)
                
                que += (node.left, col - 1),
                que += (node.right, col + 1),
                
        
        return [table[x] for x in range(minCol, maxCol + 1)]
                
            
            
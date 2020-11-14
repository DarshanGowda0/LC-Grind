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
                
            
# second attempt
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node = (0, 0, root)
        que = deque([node])
        res = []
        while que:
            # print(que)
            x, y, node = que.popleft()
            res += (x, y, node.val),
            if node.left:
                que += (x-1, y-1, node.left),
                
            if node.right:
                que += (x+1, y-1, node.right),
                
        res.sort(key = lambda x: (x[0], -x[1], x[2]))
        
        minX, maxX = res[0][0], res[-1][0]
        ans = [[] for _ in range(maxX-minX+1)]
        for x, y, val in res:
            ans[x - minX] += val,
            
        return ans
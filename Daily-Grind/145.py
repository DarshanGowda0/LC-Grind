# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # search target node
        # once found, start bfs or dfs with child as dist1 and parent as dist1
        
        def dfs(node, par):
            node.par = par
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
                
        dfs(root, None)
        
        que = deque([(target, 0)])
        seen = {target}
        while que:
            node, dist = que.popleft()
            # print(node.val if node else None)
            if dist == K:
                return [node.val] + [temp.val for temp, _ in que]
            for nbr in (node.left, node.right, node.par):
                if nbr and nbr not in seen:
                    seen.add(nbr)
                    que += (nbr, dist+1),
        return []
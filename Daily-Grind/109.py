# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        
        vals = []
        def preorder(root):
            if root:
                vals.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)
        return ",".join(map(str,vals))

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        
        vals = deque(map(int, data.split(",")))
        def dfs(min=float('-inf'), max=float('inf')):
            if vals and min < vals[0] < max:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = dfs(min, val)
                node.right = dfs(val, max)
                return node
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        arr = []
        que = deque([root])
        while que:
            node = que.popleft()
            arr += node.val if node else None,
            if node:
                que += node.left,
                que += node.right,
        # print(arr)
        return ",".join(map(str,arr))
        

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        arr = deque(data.split(","))
        
        root = TreeNode(int(arr.popleft()))
        nodeQue = deque([root])
        while arr:
            # print(arr)
            node = nodeQue.popleft()
            if node:
                left, right = arr.popleft(), arr.popleft()
                node.left = None if left == 'None' else TreeNode(int(left))
                node.right = None if right == 'None' else TreeNode(int(right))
                nodeQue += node.left, 
                nodeQue += node.right,
      
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
from collections import deque

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return root
        
        rootNode = TreeNode(root.val)
        que = deque([(rootNode, root)])
        
        while que:
            treeNode, node = que.popleft()
            prevNode = None
            headNode = None
            for child in node.children:
                newNode = TreeNode(child.val)
                que += (newNode, child),
                if not headNode:
                    headNode = newNode
                else:
                    prevNode.right = newNode
                prevNode = newNode
            treeNode.left = headNode
        
        return rootNode
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return data
        
        rootNode = Node(data.val, [])
        que = deque([(rootNode, data)])
        
        while que:
            node, treeNode = que.popleft()
            
            child = treeNode.left
            
            while child:
                newNode = Node(child.val, [])
                que += (newNode, child),
                node.children += newNode,
                child = child.right
        
        return rootNode
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
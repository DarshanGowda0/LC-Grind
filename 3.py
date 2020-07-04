class Node:
    def __init__(self, key = None, val = None, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        
        self.head.right = self.tail
        self.tail.left = self.head
    
    def addHead(self, node: Node):
        node.right = self.head.right
        node.left = self.head
        
        self.head.right.left = node
        self.head.right = node
    
    def removeNode(self, node: Node):
        left = node.left
        right = node.right
        left.right = right
        right.left = left
        return node
    
    def removeTail(self):
        if self.tail.left != self.head:
            return self.removeNode(self.tail.left)
        return -1
    
    def moveToHead(self, node: Node):
        node = self.removeNode(node)
        self.addHead(node)
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity    
        self.map = {}
        self.linkedList = LinkedList()

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.linkedList.moveToHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            node = Node(key, value)
            self.linkedList.addHead(node)
            self.map[key] = node
            if len(self.map) > self.capacity:
                node = self.linkedList.removeTail()
                del(self.map[node.key])
        else:
            node = self.map[key]
            node.val = value
            self.linkedList.moveToHead(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
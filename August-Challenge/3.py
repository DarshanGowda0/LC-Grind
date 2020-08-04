class Node:
    def __init__(self, val= None, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, val):
        node = Node(val)
        if self.head:
            cur = self.head
            prev = None
            while cur:
                prev = cur
                cur = cur.next
            prev.next = node
        else:
            self.head = node
        
    def search(self,val) -> bool:
        cur = self.head
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False
    
    def delete(self, val):
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        
        cur = self.head
        prev = None
        while cur:
            if cur.val == val:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.arr = [LinkedList() for _ in range(self.size)]
        
    def hash(self, key):
        return key % self.size
        

    def add(self, key: int) -> None:
        idx = self.hash(key)
        if not self.contains(key):
            self.arr[idx].insert(key)

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        self.arr[idx].delete(key)
        

    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        return self.arr[idx].search(key)
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
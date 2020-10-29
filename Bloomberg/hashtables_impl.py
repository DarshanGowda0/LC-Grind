from abc import ABC, abstractmethod

class HashMap(ABC):

    @abstractmethod
    def put(self, key, val):
        pass
    
    @abstractmethod
    def get(self, key):
        pass
    
    @abstractmethod
    def delete(self, key):
        pass
    
    @abstractmethod
    def exists(self, key):
        pass

    @abstractmethod
    def hash(self, key):
        pass

# hashmap impl without collission handling

class HashMapNaive(HashMap):
    def __init__(self):
        self.capacity = 103
        self.table = [None] * self.capacity

    def put(self, key, val):
        idx = self.hash(key)
        self.table[idx] = (key, val)

    def get(self, key):
        if self.exists(key):
            idx = self.hash(key)
            return self.table[idx][1]
        else:
            raise Exception("Key not found!")
    
    def delete(self, key):
        if self.exists(key):
            idx = self.hash(key)
            self.table[idx] = None
        else:
            raise Exception("Key not found!")
    
    def exists(self, key):
        idx = self.hash(key)
        return self.table[idx] and self.table[idx][0] == key

    def hash(self, key):
        return key % self.capacity

class Node:
    def __init__(self, key=None, val=None, nxt=None):
        self.key = key
        self.val = val
        self.nxt = nxt

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head:
            self.head = node
        cur = self.head
        prev = None
        while cur:
            prev = cur
            cur = cur.next
        prev.next = node

    def search(self, key):
        cur = self.head
        while cur:
            if cur.key == key:
                return True
            cur = cur.next

        return False

    def get(self, key):
        if self.search(key):
            cur = self.head
            while cur:
                if cur.key == key:
                    return cur
                   


    def delete(self, key):
        cur = self.head
        if cur and cur.key == key:
            self.head = self.head.next
            return

        prev = None
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

# hashmap impl with chaining
class HashMapC(HashMap):

    def __init__(self):
        self.capacity = 103
        self.table = [None] * self.capacity

    def put(self, key, val):
        node = Node(key, val)
        idx = self.hash(key)
        if not self.table[idx]:
            ll = LinkedList()
            ll.insert(node)
            self.table[idx] = ll
        else:
            ll = self.table[idx]
            ll.insert(node)
    
    def get(self, key):
        if self.exists(key):
            idx = self.hash(key)
            ll = self.table[idx]
            return ll.get(key)
        else:
            raise Exception("Key not found!")
    
    def delete(self, key):
        if self.exists(key):
            idx = self.hash(key)
            ll = self.table[idx]
            ll.delete(key)
        else:
            raise Exception("key not found!")
    
    def exists(self, key):
        idx = self.hash(key)
        if not self.table[idx]:
            return False
        ll = self.table[idx]
        return ll.search(key)

    def hash(self, key):
        return key % self.capacity

# hashmap impl with open addressing (linear probing)

class HashMapL(HashMap):

    def __init__(self):
        self.capacity = 103
        self.table = [None] * self.capacity

    def put(self, key, val):
        idx = self.hash(key)
        while self.table[idx]:
            idx = (idx+1)*self.capacity
        self.table[idx] = (key, val)
    
    def get(self, key):
        
        if self.exists(key):
            idx = self.hash(key)
            while self.table[idx][0] != key:
                idx = (idx+1)*self.capacity
            return self.table[idx][1]
        else:
            raise Exception("key not found!")
    
    def delete(self, key):
        if self.exists(key):
            idx = self.hash(key)
            while self.table[idx][0] != key:
                idx = (idx+1)*self.capacity
            self.table[idx] = 'D'
        else:
            raise Exception("key not found!")
    
    def exists(self, key):
        idx = self.hash(key)
        while self.table[idx] != None or self.table[idx] != 'D':
            if self.table[idx][0] == key:
                return True
            idx = (idx+1)*self.capacity
        return False

    def hash(self, key):
        return key % self.capacity


# hashmap impl with double hashing

class HashMapD(HashMap):
    def __init__(self):
        self.capacity = 103
        self.table = [None] * self.capacity
        self.prime = 87

    def put(self, key, val):
        idx = self.hash(key)
        if self.table[idx]:
            i = 1
            while True:
                idx2 = (idx + i * self.hash2(key)) % self.capacity
                if not self.table[idx2]:
                    self.table[idx2] = (key, val)
                    break
                i += 1
        else:
            self.table[idx] = (key, val)
    
    def get(self, key):
        i = 0
        idx = (self.hash(key) + i * self.hash2(key)) % self.capacity
        while self.table[idx]:
            if self.table[idx] == key:
                return self.table[idx][1]
            i += 1
            idx = (self.hash(key) + i * self.hash2(key)) % self.capacity
        raise Exception("Key not found!")
    
    def delete(self, key):
        i = 0
        idx = (self.hash(key) + i * self.hash2(key)) % self.capacity
        while self.table[idx]:
            if self.table[idx] == key:
                self.table[idx] = None
                return
            i += 1
            idx = (self.hash(key) + i * self.hash2(key)) % self.capacity
        raise Exception("Key not found!")
            
    
    def exists(self, key):
        i = 0
        idx = (self.hash(key) + i * self.hash2(key)) % self.capacity
        while self.table[idx]:
            if self.table[idx] == key:
                return True
            i += 1
            idx = (self.hash(key) + i * self.hash2(key)) % self.capacity
        return False

    def hash(self, key):
        return key % self.capacity

    def hash2(self, key):
        return self.prime - (key % self.prime)



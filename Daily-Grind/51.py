import math

class ListNode:
    def __init__(self, val = 0, next=None, minSoFar=0):
        self.val = val
        self.minSoFar = minSoFar
        self.next = next

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = ListNode(minSoFar=float('inf'))
        
    def print(self):
        cur = self.head
        while cur:
            print("{}-{}".format(cur.val, cur.minSoFar), end="=>")
            cur = cur.next
        print()

    def push(self, x: int) -> None:
        node = ListNode(val=x, next=self.head, minSoFar=min(self.head.minSoFar,x))
        self.head = node

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val
        
    def getMin(self) -> int:
        return self.head.minSoFar

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
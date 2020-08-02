"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    def print(self, head):
        cur = head
        while cur:
            print("({}-{})".format(cur.val, cur.random.val if cur.random else None),end="=>")
            cur = cur.next
        print("None")
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        # default condition
        if not head:
            return head
        
        # make clone nodes next to original nodes
        
        cur = head
        
        while cur:
            clone = Node(cur.val, cur.next, cur.random)
            cur.next = clone
            cur = clone.next
        
        # loop again and make random nodes point to next nodes
        cur = head
        while cur:
            clone = cur.next
            clone.random = clone.random.next if clone.random else None
            cur = clone.next
        
        # loop again and seperate original list from clone list
        cur,clone = head, head.next
        cloneHead = clone
        while cur:
            cur.next = clone.next
            clone.next = clone.next.next if clone.next else None
            cur, clone = cur.next, clone.next
            
        return cloneHead

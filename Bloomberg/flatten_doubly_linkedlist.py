"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # visit each node, check for child
        # if child, make a recur call which returns last node in that lList
        # attach curNode to child and lastNode of child to next
        
        def returnTail(node: 'Node'):
            # print("calling tail on ", node.val)
            cur = node
            prev = None
            while cur:
                # print("on cur", cur.val)
                if cur.child:
                    # print("has child", cur.child.val)
                    tail = returnTail(cur.child)
                    # print("got tail", tail.val)
                    nxt = cur.next
                    cur.child.prev,cur.next = cur, cur.child
                    tail.next = nxt
                    if nxt:
                        nxt.prev = tail
                    cur.child = None
                    cur = tail
                    # print("cur after ", cur.val, cur.next.val, cur.prev.val)
                    
                prev = cur
                cur = cur.next
                
            return prev
        
        cur = head
        returnTail(cur)
        
        return head
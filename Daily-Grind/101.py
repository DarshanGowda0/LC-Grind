# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not n:
            return head
        
        # go to end and count backwards decrementing n
        # if n == 0, then delete next
        
        def recur(node, n):
            if not node:
                return n
            
            x = recur(node.next, n)
            if x == 0:
                node.next = node.next.next
                
            return x - 1
        
        x = recur(head, n)
        if x == 0:
            head = head.next
        return head
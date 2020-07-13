# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        pseudoHead = ListNode()
        head = pseudoHead
        
        t1, t2 = l1, l2
        carry = 0
        while t1 and t2:
            q, r = divmod(t1.val + t2.val + carry, 10)
            head.next = ListNode(r)
            head = head.next
            t1, t2 = t1.next, t2.next
            carry = q
        
        t1 = t1 if t1 else t2
        
        while t1:
            q, r = divmod(t1.val + carry, 10)
            head.next = ListNode(r)
            head = head.next
            t1 = t1.next
            carry = q
            
        if carry:
            head.next = ListNode(carry)
            
        return pseudoHead.next
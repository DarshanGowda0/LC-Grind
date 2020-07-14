# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListIter(self, head: ListNode) -> ListNode:
        h = head
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev
    
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp
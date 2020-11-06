# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def printList(self, head):
        while head:
            print(head.val, end="->")
            head = head.next
        print()
            
    
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        oddHead, evenHead = head, head.next
        oH, eH = oddHead, evenHead
        while eH and eH.next:
            OddNxt = eH.next
            eH.next = OddNxt.next
            oH.next = OddNxt
            oH, eH = oH.next, eH.next
        
        oH.next = evenHead
        return oddHead
        
            
            
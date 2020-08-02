# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        def reverse(root: ListNode) -> ListNode:
            prev = None
            cur = root
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            return prev
                
                
        def compareLists(head1: ListNode, head2: ListNode) -> bool:
            while head2:
                if head1.val != head2.val:
                    return False
                head1 = head1.next
                head2 = head2.next
            
            return True
            
            
        
        # find the middle
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        midPrev = slow
        midPrev.next = None
        
        reverseHead = reverse(mid)
        
        res = compareLists(head, reverseHead)
        
        midHead = reverse(reverseHead)
        midPrev.next = midHead
        
        return res
        
        
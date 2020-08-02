# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slowHead, fastHead = head, head.next
        
        while slowHead and fastHead and fastHead.next:
            if slowHead == fastHead:
                return True
            
            slowHead = slowHead.next
            fastHead = fastHead.next.next
            
        return False
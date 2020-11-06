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
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return head
        
        
        def getLength(node):
            n = 0
            while node:
                n += 1
                node = node.next
                
            return n
        
        n = getLength(head)
        k = k % n
        if not k:
            return head
        
        cur = head
        prev = None
        for _ in range(n - k):
            prev = cur
            cur = cur.next
        
        prev.next = None
        newHead = cur
        
        while cur:
            prev = cur
            cur = cur.next
        
        prev.next = head
        
        return newHead
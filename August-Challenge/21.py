# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the mid
        # reverse the second
        # interleave the two lists
        
        if not head:
            return head
        
        def printList(node: ListNode):
            cur = node
            while cur:
                print(cur.val, end="->")
                cur = cur.next
            print(cur)
        
        def divide(node: ListNode):
            
            # 1-2-3-4-5
            # s s s
            # f   f f f
            slow, fast = node, node
            while slow and fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return mid
                
        def reverse(node: ListNode):
            # 1 - 2 - 3
            prev = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        mid = divide(head)
        second = reverse(mid)
        
        # 1-2-3
        # 5-4
        # 1-5-2-4-3
        first = head
        while first and second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
                
        return head
                
                
                
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # get the length of both lists
        # add dummy zero nodes infront of the shorter list
        # use recursion to add two lists
        
        # helper functions
        def lengthOf(node: ListNode):
            if not node:
                return 0
            
            cur = node
            count = 0
            while cur:
                count += 1
                cur = cur.next
                
            return count
        
        def getZeroListOfLen(n):
            cur = ListNode()
            head = cur
            for _ in range(n - 1):
                cur.next = ListNode()
                cur = cur.next
                
            return head
        
        def attach(node1, node2):
            if not node1:
                return node2
            
            cur = node1
            prev = None
            while cur:
                prev = cur
                cur = cur.next
                
            prev.next = node2
            return node1
            
        def addTwoLists(l1: ListNode, l2: ListNode):
            # node, carry
            if not l1 or not l2:
                return None, 0
            
            node, carry = addTwoLists(l1.next, l2.next)
            _sum = l1.val + l2.val + carry
            res = ListNode(_sum % 10)
            res.next = node
            return res , _sum // 10
        
        # soln starts here
        len1 = lengthOf(l1)
        len2 = lengthOf(l2)
        
        diff = abs(len1 - len2)
        if diff:
            tHead = getZeroListOfLen(diff)
            if len1 < len2:
                l1 = attach(tHead, l1)
            else:
                l2 = attach(tHead, l2)

        resHead, carry = addTwoLists(l1, l2)
        if carry:
            temp = ListNode(carry)
            temp.next = resHead
            resHead = temp
        
        return resHead         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class MyNode():
    def __init__(self, node: ListNode):
        self.node = node
        
    def __lt__(self, other):
        return self.node.val < other.node.val
    
    def __eq__(self, other):
        return self.node.val == other.val
    
from heapq import *

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        heap = [MyNode(node) for node in lists if node]
        heapify(heap)
        
        res = ListNode()
        head = res
        while heap:
            myNode  = heappop(heap)
            node = myNode.node
            head.next = node
            head = head.next
            if node.next:
                heappush(heap, MyNode(node.next))
        return res.next
            
        
        
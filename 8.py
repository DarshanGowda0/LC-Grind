# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Pair(ListNode):
    
    def __init__(self,node:ListNode):
        self.val = node.val
        self.next = node.next
    
    def __lt__(self, other):
        return self.val < other.val
        

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        que = PriorityQueue()
        res = ListNode()
        pseudoHead = res
        
        for mList in lists:
            if mList:
                que.put(Pair(mList))
            
        while not que.empty():
            node = que.get()
            res.next = node
            if node.next:
                que.put(Pair(node.next))
            res = res.next
            
        return pseudoHead.next
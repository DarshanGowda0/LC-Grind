# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush, heappop
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # start root at 0, 0
        # left child gets -1, -1 and right gets 1, -1
        # add to min heap sorted by (xPos, node.val)
        heap = []
        def dfs(node, x, y):
            if not node:
                return
            
            heappush(heap, (x, -y, node.val))
            dfs(node.left, x-1, y-1)
            dfs(node.right, x+1, y-1)
        
        dfs(root, 0, 0)
        res = []
        while heap:
            print(heap)
            temp = heappop(heap)
            tempList = [temp[2]]
            while heap and heap[0][0] == temp[0]:
                tempList.append(heappop(heap)[2])
            res += tempList,
            
        return res
                
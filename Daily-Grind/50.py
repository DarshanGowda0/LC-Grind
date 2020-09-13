# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def dfs(node, _sum):
            if not node:
                return
            
            if node.val == _sum:
                self.count += 1
                
            dfs(node.left, _sum - node.val)
            dfs(node.right, _sum - node.val)
        
        def path(root, sum):
            if not root:
                return 0
            dfs(root, sum)
            path(root.left, sum)
            path(root.right, sum)    
        
        self.count = 0
        path(root, sum)
        return self.count

# second attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # if the sum < 0, return 0 if sum == 0, return 1, else
        # at every node subtract the sum from current value and send it down
        # start with same sum for every node
        # memoize if there are overlapping sub problems
        
        if not root:
            return 0
        
        def recur(node: TreeNode, cur: int) -> int:
            if not node:
                return
            
            nonlocal count
            
            cur += node.val
            
            if cur == sum:
                count += 1
            
            count += preSum[cur - sum]
            
            preSum[cur] += 1
            
            recur(node.left, cur)
            recur(node.right, cur)
            
            preSum[cur] -= 1
        
        count = 0
        preSum = defaultdict(int)
        recur(root, 0)
        
        return count
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # 1 (2--3--4) (5--6--7)
        # 2 3 4 # 5 6 7
        # 1 (2--3--4) (5--6---7)
        #.  2 3 4     # 5 (6--7) # 6 7
        # 1 (401--349---90--88)
        # 401 349---90 88
        
        def recur(string, dashes):
            
            if not string:
                return None
            
            exp = "(?<=\\d)[-]{" + str(dashes) + "}(?=\\d)"
            arr = re.split(exp, string)
            
            node = TreeNode(int(arr[0]))
            if len(arr) > 1:
                node.left = recur(arr[1], dashes + 1)
            if len(arr) > 2:
                node.right = recur(arr[2], dashes + 1)
            
            return node
        
        return recur(S, 1)
            
from heapq import *
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        if not tasks:
            return 0

        stasks = sorted(tasks, key=lambda x: x[1]-x[0], reverse=True)
        res = stasks.pop()[1]
        while stasks:
            a, m = stasks.pop()
            res += a
            res = max(res, m)
            
        return res
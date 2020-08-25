from collections import deque
from random import choice
class Solution:

    def __init__(self, rects):
        self.rects, self.ranges, sm = rects, [0], 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self):
        n = random.randint(0, self.ranges[-1] - 1)
        i = bisect.bisect(self.ranges, n)
        x1, y1, x2, y2 = self.rects[i - 1]
        n -= self.ranges[i - 1]
        return [x1 + n % (x2 - x1 + 1), y1 + n // (x2 - x1 + 1)]
    


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

# store all int points within the rect inside a list
# perform bfs or dfs on each list 
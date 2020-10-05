from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = map(collections.Counter, (s, t))
        return sum((c1 - c2).values())
from heapq import *

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            words = log.split()
            return (0, words[1:], words[0]) if words[1][0].isalpha() else (1,)
        return sorted(logs, key= f)
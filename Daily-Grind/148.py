from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # greedy approach
        # select the highest freq more often
        # sort by freq, allocate all highest with gaps
        # then start filling the remaining
        
        # A B _ A B _ A B
        
        counter = Counter(tasks)
        freq = sorted(counter.values())
        # print(freq)
        maxFreq = freq.pop()
        idleSlots = (maxFreq - 1) * n
        
        while freq and idleSlots >= 0:
            idleSlots -= min(maxFreq - 1, freq.pop())
            
        idleSlots = max(idleSlots, 0)
        
        return idleSlots + len(tasks)
            
            
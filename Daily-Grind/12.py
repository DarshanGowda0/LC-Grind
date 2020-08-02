from collections import defaultdict
from queue import PriorityQueue
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        
        for word in words:
            freq[word] += 1
        
        que = PriorityQueue()
        
        for key, val in freq.items():
            que.put((-val,key))
            
        ans = []
        for i in range(k):
            val, _key = que.get()
            ans += _key,
            
        return ans
from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # brute force - sort and return the kth element - O(n log n)
        # we could also use priority queue/min heap and pop till k, O(n lg n)
        # optimize on space tho, only push to heap if the ele is greater than the top ele - space - O(k) - O(k log k)
        
        heap = []
        
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            elif heap and num > heap[0]:
                heappush(heap, num)
                if len(heap) > k:
                    heappop(heap)

        
        return heap[0]
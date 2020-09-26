from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a heap, with indices, keep poping untill the index is in the window
        
        # has to be maxHeap
        heap = []
        start, end = 0, 0
        res = []
        while end < len(nums):
            # print(start, end, heap)
            heappush(heap,(-nums[end], end))
            end += 1
            
            if end - start + 1 > k:
                while heap[0][1] < start:
                    heappop(heap)
                res += -heap[0][0],
                start += 1
                
        return res
                
                
from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # use two heaps
        # store num in max heap, reverse if not maxheap or num < maxheap[0]
        # else store in minHeap, second half
        # if len(maxHeap) + 1 > len(minHeap), then pop and add to minHeap
        # if len(minHeap) > len(maxHeap) same
        
        self.minHeap, self.maxHeap = [], []
        

    # max -> [-1, ]
    # min -> [2]
        
    def addNum(self, num: int) -> None:
        # print("taking ", num)
        if not self.maxHeap or num < -self.maxHeap[0]:
            # print("into max")
            heappush(self.maxHeap, -num)
            if len(self.maxHeap) > len(self.minHeap) + 1:
                # print("moving to min")
                heappush(self.minHeap, -heappop(self.maxHeap))
        else:
            # print("into min")
            heappush(self.minHeap, num)
            if len(self.minHeap) > len(self.maxHeap):
                # print("moving to max")
                heappush(self.maxHeap, -heappop(self.minHeap))
        # print(self.maxHeap, self.minHeap)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2 + self.minHeap[0] / 2
        else:
            return -self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class MinHeap:

    # making the assumption that heap starts at idx 1

    def __init__(self):
        self.size = 0
        self.heap = [0]

    # append at end and then sift up 
    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self._sift_up(self.size)

    # take out first ele, put the last ele on root and sift down
    def delete_min(self):

        if self.size == 0:
            return None

        root = self.heap[1]
        self.heap[1] = self.heap[self.size]

        self.heap.pop()
        self.size -= 1

        self._sift_down(1)

        return root

    # compare to parent from i to root
    def _sift_up(self, idx):
        while idx // 2 > 0:
            parentIdx = idx // 2
            if self.heap[idx] < self.heap[parentIdx]:
                self.heap[parentIdx], self.heap[idx] = self.heap[idx], self.heap[parentIdx]
            idx = parentIdx

    # at every idx, if parent is greater then switch with min child and sift down recursively
    def _sift_down(self, idx):
        while idx * 2 <= self.size:
            minChild = self._get_min(idx)
            if self.heap[idx] > self.heap[minChild]:
                self.heap[idx], self.heap[minChild] = self.heap[minChild], self.heap[idx]
            idx = minChild

    def _get_min(self, idx):
        if idx * 2 + 1 > self.size:
            return idx * 2
        c1, c2 = idx*2, idx*2+1
        if self.heap[c1] < self.heap[c2]:
            return c1
        else:
            return c2
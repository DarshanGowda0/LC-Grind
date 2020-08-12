from heapq import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # naive solution is put everything in sorted array and return kth element
        # put everything in heap
        # how to optimize based on its sorted hor and vertically?
        # bidirectional visit and add to heap, once it reaches len == k, return top
        
        heap = [(matrix[0][0],0,0)]
        directions = [(1,0),(0,1)]
        seen = {(0,0)}
        n = len(matrix)
        res = []
        
        while heap:
            # print(heap)
            val, x, y = heappop(heap)
            res += val,
            if len(res) == k:
                return res[-1]
            
            for p, q in directions:
                nx, ny = x+p, y+q
                if nx < n and ny < n and (nx,ny) not in seen:
                    # print(nx, ny)
                    heappush(heap, (matrix[nx][ny], nx, ny))
                    seen.add((nx,ny))
            
        
            
        
        
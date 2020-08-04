from heapq import *

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        #1 - both are disjoint - 
        #2 - they have a overlap - [max(firstIdx), min(lastIdx)]
        #3 - one is in the other - the inner is the intersection
        
        i, j = 0, 0
        m, n = len(A), len(B)
        res = []
        while i < m and j < n:
            int1, int2 = A[i], B[j]
            if int1[1] < int2[0]:
                i+=1
                continue
            if int2[1] < int1[0]:
                j+=1
                continue
            
            overlap = [max(int1[0], int2[0]), min(int1[1], int2[1])]
            res += overlap,
            if min(int1[1], int2[1]) == int1[1]:
                i+=1
            else:
                j+=1
        
        return res
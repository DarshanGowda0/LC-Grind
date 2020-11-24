from random import randint

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def recur(points, low, high, K):
            p = partition(points, low, high)
            if p == K-1:
                return points[:K]
            
            elif p < K - 1:
                return recur(points, p + 1, high, K)
            else:
                return recur(points, low, p-1, K)
            
        
        def dist(point):
            x, y = point
            return x**2 + y**2
        
        def partition(points, low, high):
            
            rIdx = randint(low, high)
            points[rIdx], points[high] = points[high], points[rIdx]
            
            pivot = dist(points[high])
            
            for i in range(low, high):
                if dist(points[i]) < pivot:
                    points[i], points[low] = points[low], points[i]
                    low += 1
                    
            points[low], points[high] = points[high], points[low]
            
            return low
        
        return recur(points, 0, len(points) - 1, K)
            
            
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # find the peak, then do binary search on left, if found return else find on right
        
        def binarySearch(low, high, isDesc=False):
            while low <= high:
                mid = low + (high - low) // 2
                if mountain_arr.get(mid) == target:
                    return mid
                elif mountain_arr.get(mid) < target:
                    if not isDesc:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    if not isDesc:
                        high = mid - 1
                    else:
                        low = mid + 1
                        
            return -1
        
        def getPeak(low, high):
            peak = low
            while low < high:
                mid = low + (high - low) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    low = peak = mid + 1
                else:
                    high = mid
                
            return low
            
        n = mountain_arr.length()
        peak = getPeak(0, n-1)
        # print(peak)
        if target == mountain_arr.get(peak):
            return peak
        
        res = binarySearch(0, peak-1)
        if res == -1:
            res = binarySearch(peak+1, n - 1, True)
        
        return res
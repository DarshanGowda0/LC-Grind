from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # quick select
        
        def recur(nums, k, low, high):
            # print(nums[low:high+1])
            p = partition(nums, low, high)
            
            if p == k-1:
                return nums[p]
            
            if p < k - 1:
                return recur(nums, k, p+1, high)
            else:
                return recur(nums, k, low, p-1)
                
        def partition(nums, low, high):
            if low == high:
                return low
            
            pivot = nums[high]
            
            for i in range(low, high):
                if nums[i] < pivot:
                    nums[low], nums[i] = nums[i], nums[low]
                    low+=1
                    
            nums[high], nums[low] = nums[low], nums[high]
            return low
        
        return recur(nums, len(nums)-k+1, 0, len(nums)-1)
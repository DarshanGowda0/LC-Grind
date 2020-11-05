class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # use binary search to find the peak
        # if mid > 0 and nums[mid] > nums[mid] - 1, slope is rising so peak is on right
        # else slope is falling, so peak is on left
        
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            elif nums[mid] < nums[mid + 1]:
                low = mid + 1  
            else:
                return low
                
        return low
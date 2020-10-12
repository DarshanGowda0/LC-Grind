class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # binary search
        # determine if its a falling slope or rising slope
        # if its a falling slope, move left, else right
        # if a[i-1] < a[i] > a[i+1], thats the ans
        
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            # print(left, right, mid)
            if mid > 0 and arr[mid - 1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid+1]:
                right = mid - 1                
            else:
                left = mid + 1
                
        
            
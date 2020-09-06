class Solution:
    def findMin(self, nums: List[int]) -> int:
        # take mid and see if mid > start, then min is on right
        # 4 5 6 7 0 1 2 
        # else the min is on left
        # 6 7 0 1 2 3 4 
        low, high = 0, len(nums) - 1
        while low < high and nums[low] > nums[high]:
            mid = low + (high - low) // 2
            # print(nums[mid])
            if nums[low] <= nums[mid]:
                # left is sorted, so min is on right
                low = mid + 1
            else:
                high = mid
        
        return nums[low]
    
        
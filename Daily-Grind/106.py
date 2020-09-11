class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # naive is search linear- O(n)
        # modified binary search
        # 4 5 6 7 0 1 2 - 0
        
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1
                
# second attempt
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the list is still sorted  in asc, but has a pivot point
        # use modified binary search
        # if nums[left] < nums[mid] -> everything on left is sorted and right is unsorted
        
        # [5,1,2,3,4]
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (end - start)//2 + start
            # print(mid)
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                # everything on left is sorted
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
                    
            else:
                # everything on right is sorted
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
            # print(start, end)
        return -1
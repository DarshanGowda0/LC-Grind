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
                
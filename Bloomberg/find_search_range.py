class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums, start, end, target, findMax=False):
            idx = -1
            while start <= end:
                # print(start, end)
                mid = start + (end - start) // 2
                # print(mid)
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    idx = mid
                    if findMax:
                        start = mid + 1
                    else:
                        end = mid - 1
                        
            return idx
                   
        res = [-1, -1]
        n = len(nums)
        res[0] = search(nums, 0, n-1,target)
        if res[0] != -1:
            res[1] = search(nums, 0, n-1, target, True)
        
        return res
                        
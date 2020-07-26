class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort - n log n
        nums.sort()
        n = len(nums)
        
        ans = set()
        # start i = 0 to n - O(n)
        for i in range(n):
            if nums[i] > 0:
                break
        # j = i+1, k = n - 1, do binary search - O(log n)
            j = i+1
            k = n-1
            # print(i)
            while j < k:
                # print("j {}, k {}".format(j, k))
                tempSum = nums[i] + nums[j] + nums[k]
                if tempSum == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif tempSum > 0:
                    k -= 1
                else:
                    j += 1
            
        return ans
        
        
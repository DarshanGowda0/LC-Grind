class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        
        for num in numSet:
            if num - 1 not in numSet:
                cur = num
                streak = 1
                
                while cur+1 in numSet:
                    cur = cur+1
                    streak+=1
                
                ans = max(ans, streak)
                
        return ans


# second attempt

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # scan once and add in hashset
        # scan again and start counting if i - 1 is not present
        
        ans = 0
        seen  = set(nums)
        for num in nums:
            if num in seen and num - 1 not in seen:
                temp, i = 0, num
                while i in seen:
                    temp+=1
                    i+=1
                ans = max(ans, temp)
        
        return ans
                    
            
        
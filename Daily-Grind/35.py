class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        i, j = 0, len(height)-1
        
        while i < j:
            area = max(area, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        
        return area
            

# second attempt
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers technique
        # area is l*b, so decrement width only when height increases
        
        left, right = 0, len(height)-1
        ans = float('-inf')
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
                
        return ans
            
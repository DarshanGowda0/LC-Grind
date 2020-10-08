class Solution:
    def maxArea(self, height: List[int]) -> int:
        # take two pointers
        # if we decrease the x axis, then the gain should be with Y axis
        # so always move on the lower Y axis and compare to global max area
        
        i, j = 0, len(height) - 1
        maxArea = float('-inf')
        while i < j:
            
            maxArea = max(maxArea, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
                
        return maxArea

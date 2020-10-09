class Solution:
    def trap(self, height: List[int]) -> int:
        # 0 1 1 2 2 2 2 3 3 3 3 3
        # 3 3 3 3 3 3 3 3 2 2 2 1
        # 0 0 1 0 1 2 1 0 0 1 0 0
        
        leftArr = height[:]
        rightArr = height[:]
        
        for i in range(1, len(height)):
            leftArr[i] = max(leftArr[i-1], leftArr[i])
            
        for i in range(len(height) - 2,-1,-1):
            rightArr[i] = max(rightArr[i+1], rightArr[i])
            
        res = 0
        for l, r, h in zip(leftArr, rightArr, height):
            res += min(l, r) - h
            
        return res
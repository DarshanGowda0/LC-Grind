class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        lArr = [i for i in height]
        rArr = [i for i in height]
        
        for i in range(1, len(lArr)):
            lArr[i] = max(lArr[i-1], lArr[i])
        
        for i in range(len(rArr) - 2, -1, -1):
            rArr[i] = max(rArr[i], rArr[i+1])
            
        res = 0
        for l, r, h in zip(lArr, rArr, height):
            res += min(l,r) - h
            
        return res
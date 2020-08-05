class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        highBit = 1
        
        while n != 0:
            res += (n & 1)
            n >>= 1
        
        return res
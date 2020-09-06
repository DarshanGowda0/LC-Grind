class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        msb = 31
        while n > 0:
            ans += (n&1) << msb
            msb -= 1
            n >>= 1
        
        return ans
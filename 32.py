class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num +1)
        i, b = 0, 1
        while b <= num:
            while i < b and i+b <= num:
                res[i+b] = res[i] + 1
                i += 1
            
            # reset
            i = 0    
            b <<= 1
        
        return res
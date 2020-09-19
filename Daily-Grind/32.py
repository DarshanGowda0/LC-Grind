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


# second attempt

class Solution:
    def countBits(self, num: int) -> List[int]:
        # 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 10000
        # 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16
        # 0    1    1    2    1    2    2    3    1    2    2    3    2    3    3    4    1
        # 0    1    0+1  1+1  0+1  1+1  1+1  2+1  0+1  1+1  1+1  2+1  1+1  2+1  2+1  3+1  0+1
    #i              2         4                   8                                       16
    #j    0    1    0    1    0    1    2    3    0    1    2    3    4    5    6    7    0   
        
        if num == 0:
            return [0]
        
        res = [0] * (num+1)
        res[0], res[1] = 0, 1
        
        i = 2
        while i <= num:
            # print("i", i)
            j, n = 0, i << 1
            while i+j < n and i+j <= num:
                # print("j", j, "i+j", i+j, res)
                res[i+j] = res[j] + 1
                j+=1
            i = n
            
        return res
        
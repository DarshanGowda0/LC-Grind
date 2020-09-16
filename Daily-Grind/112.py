class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        x , y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)
        
        sign = 1 if a > 0 else -1
        
        if a * b > 0:
            while y:
                ans = x ^ y
                carry = (x&y) << 1
                x,y = ans, carry
        else:
            while y:
                ans = x ^ y
                bor = ((~x) & y) << 1
                x, y = ans, bor


        return sign * x
            
        
# second attempt
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # binary addition
        # 1 + 0 / 0 + 1 = 1
        # 0 + 0 = 0
        # 1 + 1 = 10
        
        # sum = xor and carry = and
        # 100
        # 101
        # 
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)
        
        sign = 1 if a > 0 else - 1
        
        if a*b > 0:
            while y:
                s = x ^ y
                c = (x & y) << 1
                x, y = s, c
        else:
            while y:
                s = x ^ y
                bo = (~x & y) << 1
                x, y = s, bo
                
        return sign * x

        return a
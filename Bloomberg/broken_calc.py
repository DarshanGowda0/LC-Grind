class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        # go reverse
        # if y is odd, add 1 to make it even
        # if y is even and > x, divide it
        
#         if Y == X:
#             return 0
        
#         # odd
#         if Y % 2 == 1 or Y < X:
#             return 1 + self.brokenCalc(X, Y+1)
        
#         # even and greater
#         # if Y > X:
#         return 1 + self.brokenCalc(X, Y // 2)
    
        ans = 0
        while Y > X:
            if Y % 2 == 1:
                Y = Y + 1
            else:
                Y = Y // 2
            ans += 1
            
        return ans + X - Y
    
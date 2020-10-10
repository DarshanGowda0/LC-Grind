# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        
        def count(x, X, y, Y):
            if x > X or y > Y or not sea.hasShips(Point(X, Y), Point(x, y)):
                return 0
            if (x, y) == (X, Y):
                return 1
            xm = (x + X) // 2
            ym = (y + Y) // 2
            xRanges = (x, xm), (xm+1, X)
            yRanges = (y, ym), (ym+1, Y)
            return sum(count(xr[0], xr[1], yr[0], yr[1]) for xr in xRanges for yr in yRanges)
        return count(bottomLeft.x, topRight.x, bottomLeft.y, topRight.y)
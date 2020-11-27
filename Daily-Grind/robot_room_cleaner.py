# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def recur(cell = (0,0), d = 0):
            visited.add(cell)
            robot.clean()
            
            for i in range(4):
                newD = (d+i) % 4
                nextCell = (cell[0]+directions[newD][0], cell[1]+directions[newD][1])
                
                if nextCell not in visited and robot.move():
                    recur(nextCell, newD)
                    goBack()
                    
                robot.turnRight()
                
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        visited = set()
        recur()
            
            
            
            
            
            
            
            
            
            
            
            
            
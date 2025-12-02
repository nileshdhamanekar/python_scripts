# https://leetcode.com/problems/robot-bounded-in-circle/
# Resource: https://www.youtube.com/watch?v=t6nUzD41G5U
# Not sure why this works in case where multiple repeatations of the string needs to happen.
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        d = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for char in instructions:
            if char == "G":
                x += directions[d%4][0]
                y += directions[d%4][1]
            elif char == "R":
                d += 1
            elif char == "L":
                d -= 1
            
        return (x,y) == (0,0) or d%4 != 0
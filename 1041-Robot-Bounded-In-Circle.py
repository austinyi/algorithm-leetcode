class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir = 0
        dx, dy = 0, 0
        for i in instructions:
            if i == "L":
                dir -= 1
            elif i == "R":
                dir += 1
            else:
                if dir % 4 == 0:
                    dy += 1
                elif dir % 4 == 1:
                    dx += 1
                elif dir % 4 == 2:
                    dy -= 1
                else:
                    dx -= 1
        
        if dir % 4 != 0:
            return True
        elif dx == 0 and dy == 0:
            return True
        else:
            return False

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direc = ((0, 1), (1, 0), (0, -1), (-1, 0))
        drc = 0
        x = y = 0
        for i in instructions:
            if i == 'G':
                x += direc[drc][0]
                y += direc[drc][1]
            elif i == 'L':
                drc = (drc - 1) % 4
            else :
                drc = (drc + 1) % 4
        return (x, y) == (0, 0) or drc != 0
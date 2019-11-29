class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return True if moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D') else False
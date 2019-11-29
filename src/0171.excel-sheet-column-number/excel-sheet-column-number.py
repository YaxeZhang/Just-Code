from functools import reduce
class Solution:
    def titleToNumber(self, s: str) -> int:
        return reduce(lambda r, c: 26*r + ord(c)-64, s, 0)
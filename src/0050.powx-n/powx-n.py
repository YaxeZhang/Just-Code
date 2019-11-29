class Solution:
    def myPow(self, x: float, n: int) -> float:
        p, r = abs(n), 1
        while p:
            if p & 1:
                r *= x
            x *= x
            p >>= 1
        return r if n >= 0 else 1/r
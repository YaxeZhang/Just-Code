class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m and m != n:   # NOTE: break when m == 0
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift
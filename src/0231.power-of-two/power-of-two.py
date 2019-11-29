class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 1073741824 % n == 0
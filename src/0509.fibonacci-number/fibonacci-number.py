class Solution:
    def fib(self, N: int) -> int:
        g = (1 + 5 ** 0.5) / 2
        return int((g ** N + 1) / 5 ** 0.5)
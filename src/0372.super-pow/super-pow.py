class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = int(''.join(map(str, b)))
        r = 1
        while b:
            if b & 1:
                r = r*a % 1337
            a = a*a % 1337
            b >>= 1
        return r
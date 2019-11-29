class Solution:
    def isUgly(self, num: int) -> bool:
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1
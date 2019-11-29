class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n < 1:
            return 1
        if n > 10:
            return 0
        ret = cur = d = 9
        for _ in range(n - 1):
            cur *= d
            ret += cur
            d -= 1
        return ret + 1
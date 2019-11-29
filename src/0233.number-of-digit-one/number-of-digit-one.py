class Solution:
    def countDigitOne(self, n):
        cnt, i = 0, 1
        while i <= n:
            a, b = n // i, n % i
            cnt += (a+8) // 10 * i + (a%10 == 1) * (b+1)
            i *= 10
        return cnt
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, carry, i, j = [], 0, len(num1), len(num2)
        while i or j or carry:
            if i:
                carry += int(num1[i-1])
                i -= 1
            if j:
                carry += int(num2[j-1])
                j -= 1
            res.append(str(carry % 10))
            carry //= 10
        return ''.join(res[::-1])
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        i = j = len(n) - 1
        while i and n[i-1] >= n[i]:
            i -= 1
        if not i:
            return -1
        while n[j] <= n[i-1]:
            j -= 1
        n[i-1], n[j] = n[j], n[i-1]
        n = int(''.join(n[:i] + n[i:][::-1]))
        return n if 1 < n < 2**31-1 else -1
        
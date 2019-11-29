class Solution:
    def maximalSquare(self, A):
        area = 0
        if A:
            p = [0] * len(A[0])
            for row in A:
                s = list(map(int, row))
                for j, c in enumerate(s[1:], 1):
                    if s[j]:
                        s[j] = min(p[j-1], p[j], s[j-1]) + 1
                area = max(area, max(s) ** 2)
                p = s
        return area
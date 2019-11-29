class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [0] * len(A)
        i, j = 0, len(A) - 1
        while i <= j:
            left, right = A[i], A[j]
            if abs(left) > abs(right):
                ans[j - i] = left ** 2
                i += 1
            else:
                ans[j - i] = right ** 2
                j -= 1
        return ans
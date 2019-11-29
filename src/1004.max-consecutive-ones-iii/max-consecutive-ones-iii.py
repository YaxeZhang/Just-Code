class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return len(A) - i
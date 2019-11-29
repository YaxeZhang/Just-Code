class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        c = len(A)
        dp = [float('inf')] + A[c-1][:] + [float('inf')]
        for i in range(c-2, -1, -1):
            tmp = [A[i][j-1] + min(dp[j-1], dp[j], dp[j+1]) for j in range(1, c+1)]
            dp[1:c+1] = tmp
        return min(dp)
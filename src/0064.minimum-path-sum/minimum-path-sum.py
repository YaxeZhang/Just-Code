class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0][:]
        for i in range(1, n):
            dp[i] += dp[i-1]
        for i in range(1, m):
            for j in range(n):
                if j > 0:
                    dp[j] = grid[i][j] + min(dp[j], dp[j-1])
                else:
                    dp[j] = grid[i][j] + dp[j]
        return dp[-1]
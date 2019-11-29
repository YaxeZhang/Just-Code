class Solution:
    def minDistance(self, w1, w2):
            m, n = len(w1), len(w2)
            dp = [[0] * (n + 1) for i in range(m + 1)]
            for i in range(m):
                for j in range(n):
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (w1[i] == w2[j]))
            return m + n - 2 * dp[m][n]
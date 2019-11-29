class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val < matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < m - 1 and val < matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val < matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < n - 1 and val < matrix[i][j + 1] else 0)
            return dp[i][j]
                
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        return max(dfs(x, y) for x in range(m) for y in range(n))
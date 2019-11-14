### 矩阵中找最长上升路径
#### 题目
给定一个整数矩阵，找到最长的增长路径的长度。 在每个单元格中，您可以向四个方向移动：向左，向右，向上或向下。 您不得对角移动或移动到边界之外（即不允许环绕）。
#### 解法
**分析：** 记忆化 DFS ，第一次接触的话想不到，不过接触过就很简单。

```python
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
```

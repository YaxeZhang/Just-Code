<span id = "00"></span>
## DFS & BFS
 - [200. Number of Islands](#200-number-of-islands)
 - [286	Walls and Gates]
 - [130	Surrounded Regions]
 - [339	Nested List Weight Sum]
 - [364	Nested List Weight Sum II]
 - [127	Word Ladder]
 - [51	N-Queens]
 - [52	N-Queens II]
 - [126	Word Ladder II]

## 200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

给定二维地图“ 1”（土地）和“ 0”（水），计算岛屿的数量。 一个岛屿被水包围，是通过水平或垂直连接相邻的陆地而形成的。 您可以假设网格的所有四个边缘都被水包围。

**Example**

```
Input:
11110
11010
11000
00000

Output: 1

Input:
11000
11000
00100
00011

Output: 3
```

---

### Python Solution
**分析：** 一种是改变原矩阵的方法，另一种是不改变矩阵的方法，但是有额外的 O(M*N) 的空间需求。

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        ans = 0

        def dfs(i, j):
            grid[i][j] = 2
            if i > 0 and grid[i - 1][j] == '1':
                dfs(i-1, j)
            if i < len(grid) - 1 and grid[i + 1][j] == '1':
                dfs(i+1, j)
            if j > 0 and grid[i][j - 1] == '1':
                dfs(i, j - 1)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
                dfs(i, j + 1)
            return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1
        return ans
```

**需要额外空间但不改变原矩阵**

```Python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        directions = [(-1, 0), (0, -1), (+1, 0), (0, +1)]
        visited = set()
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    stack = [(i, j)]
                    res += 1            
                    while stack:
                        x, y = stack.pop()
                        visited.add((x, y))
                        for d_x, d_y in directions:
                            x_d, y_d = x + d_x, y + d_y
                            if 0 <= x_d < len(grid) and 0 <= y_d < len(grid)[i] and grid[x_d][y_d] == "1" and (x_d, y_d) not in visited:
                                stack.append((x_d, y_d))

        return res
```

[返回目录](#00)

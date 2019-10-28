<span id = "00"></span>
## DFS & BFS
 - [200. Number of Islands](#200-number-of-islands)
 - [286	Walls and Gates]
 - [130. Surrounded Regions](#130-surrounded-regions)
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

## 130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

给定一个包含“ X”和“ O”（字母O）的2D板，捕获被“ X”包围的所有区域。

通过将所有“ O”翻转到该包围区域中的“ X”来捕获区域。

**Example**

```
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
```

---

### Python Solution
**分析：** 此题类似于围棋，就是先落子最后判断哪些被吃掉了。解决方法分为 DFS 和 BFS 两种。

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if board[i][j] == 'O':
                board[i][j] = 'D'
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < m and 0 <= y < n:
                        dfs(x, y)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)

        for x in range(m):
            for y in range(n):
                if board[x][y] == 'D':
                    board[x][y] = 'O'
                else:
                    board[x][y] = 'X'
```

**BFS**

```Python
from collections import deque

class Solution:

    def bfs(self, board, start_i, start_j):
        m, n = len(board), len(board[0])

        q = deque()
        q.append((start_i,start_j))

        while q:
            i, j = q.popleft()

            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 's'
                q.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return

        # go round the border and run bfs from every 'O' found, those 'O's found
        # by the bfs stay - encoded 's'
        m, n = len(board), len(board[0])


        for i in range(m):
            if board[i][0] == 'O':
                self.bfs(board, i, 0)
            if board[i][n-1] == 'O':
                self.bfs(board, i, n-1)

        for j in range(n):
            if board[0][j] == 'O':
                self.bfs(board, 0, j)
            if board[m-1][j] == 'O':
                self.bfs(board, m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 's':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
            
```

[返回目录](#00)

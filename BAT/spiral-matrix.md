### 顺时针打印矩阵
#### 题目
给定一个m x n元素的矩阵（m行，n列），以螺旋顺序返回矩阵的所有元素。
#### 解法
**分析：** 重点在于考虑步进方向和边界条件。

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix: return res
        x = y = i = 0
        delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
        pos = [0, 0, len(matrix[0])-1, len(matrix)-1] # 左、上、右、下。后面懒得判断推出来的。
        while pos[0] <= pos[2] and pos[1] <= pos[3]:
            while pos[0] <= y <= pos[2] and pos[1] <= x <= pos[3]:
                res.append(matrix[x][y])
                x, y = x+delta[i][0], y+delta[i][1]
            x, y = x-delta[i][0], y-delta[i][1]
            i = (i+1) % 4
            pos[i] += sum(delta[i])
            x, y = x+delta[i][0], y+delta[i][1]
        return res
```

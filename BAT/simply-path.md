### 交换之后的最大值
#### 题目
给定一个非负整数，您最多可以交换两个数字一次以获得最大值。返回您可以获得的最大值。
#### 解法
**分析：** 从后往前遍历，记录最大和相对小索引，最后交换。

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        max_idx = len(num) - 1
        xi = yi = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[max_idx]:
                max_idx = i
            elif num[i] < num[max_idx]:
                xi = i
                yi = max_idx
        num[xi], num[yi] = num[yi], num[xi]
        return int("".join(num))
```

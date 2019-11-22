### 最长的连续1
#### 题目
给定一个0和1的数组A，我们最多可以将K值从0更改为1。 返回仅包含1的最长（连续）子数组的长度。
#### 解法
**分析：** 用 K 来保持一个滑动窗口，并且 j-i+1 保持的是目前最大的连续 1 的子数组长度。如果有更长的就会把之前的坑填上，如果没有那么这就是最长的子数组长度。

```python
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return len(A) - i
```

### 具有最大乘积的连续子数组
#### 题目
给定一个整数数组nums，查找具有最大乘积的数组（至少包含一个数字）中的连续子数组。
#### 解法
**分析：** A 是前缀乘积，B 是后缀乘积。找到最大的那个就可以了。很巧妙的解法。

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rev = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            rev[i] *= rev[i-1] or 1
        return max(nums + rev)
```

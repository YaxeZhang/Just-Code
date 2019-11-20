### 第一次缺失的正数
#### 题目
给定一个未排序的整数数组，找到最小的缺失正整数。
#### 解法
**分析：** 先把他们尽量换到自己的位置上，直到不能换为止，然后遍历一遍找到第一个不满足的数字。

```python
class Solution:
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
        return len(nums) + 1
```

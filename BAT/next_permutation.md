### 下一个排列
#### 题目
实现下一个排列，将字典重新排列成数字的下一个更大的排列。 如果无法进行这种安排，则必须将其重新排列为最低可能的顺序（即，以升序排列）。 替换必须使用 O(1) 的空间并且仅使用恒定的额外内存。
#### 解法
**分析：** 感觉这道题如果面试遇到没有做过的话很容易黑，重点是讲解自己思考的过程和可能的想法。

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums) - 1
        while i and nums[i] <= nums[i-1]:
            i -= 1
        if i > 0:
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = reversed(nums[i:])
```

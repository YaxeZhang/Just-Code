### 40.最大的第k个数
#### 题目描述
在未排序的数组中找到第k个大的元素。 请注意，它们是排序顺序中第k个大的元素，而不是第k个不同的元素。
#### 解法：
**分析：** 快排，选择排序，堆排序。这道题考察的是排序算法的应用。可能会手写堆排序。

```python
class Solution:  # 赖皮的排序，实际是快排。
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
```

```python
class Solution:  # 选择排序，选出前 k 个就足够了，但很慢。
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            tmp = i
            for j in range(i+1, len(nums)):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[i], nums[tmp] = nums[tmp], nums[i]
        return nums[k-1]
```

```python
class Solution:  # 堆排序。
    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest4(self, nums, k):
      heapq.heapify(nums)
      for _ in range(len(nums)-k):
          heapq.heappop(nums)
      return heapq.heappop(nums)

    # O(k+(n-k)lgk) time, min-heap        
    def findKthLargest5(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
```

```python
from random import randint
class Solution(object):  # 快速排序。
    def findKthLargest(self, nums, k):
        def partition(l, r):
            ri = randint(l, r)
            nums[r], nums[ri] = nums[ri], nums[r]
            for i, v in enumerate(nums[l: r+1], l):
                if v >= nums[r]:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            return l - 1

        l, r, k = 0, len(nums) - 1, k - 1
        while True:
            pos = partition(l, r)
            if pos < k:
                l = pos + 1
            elif pos > k:
                r = pos - 1
            else:
                return nums[pos]
```

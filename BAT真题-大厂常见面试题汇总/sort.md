
### 冒泡排序
#### 题目描述
冒泡排序给定数组。
#### Python Solution：
**分析：**

```Python
class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+
1], nums[j]
        return nums
```

**可以优化内层和外层嵌套：**  flag 用来优化外层嵌套， k 和 pos 用来优化内层嵌套。

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        pos, k = 0, len(nums) - 1
        for i in range(len(nums)-1):
            flag = 0
            for j in range(k):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+
1], nums[j]
                    flag, pos = 1, j
            k = pos
            if flag == 0:
                return nums
        return nums
```

**再优化，双向寻找最小最大值：**  

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        pos, k = 0, len(nums) - 1
        for i in range(len(nums)-1):
            flag = 0
            for j in range(k):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    pos = j
                    flag = 1
            if not flag:
                return nums
            k = pos
            for j in range(k-1, 0, -1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    flag = 1
        return nums
```

[返回目录](#501)

---

### 插入排序
#### 题目描述
插入排序给定数组。
#### Python Solution：
**分析：**

```Python
class Solution:
    def insertionSort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums
```

[返回目录](#502)

---

### 选择排序
#### 题目描述
选择排序给定数组。
#### Python Solution：
**分析：**

```Python
class Solution:
    def selectionSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            minIdx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minIdx]:
                    minIdx = j
            nums[minIdx], nums[i] = nums[i], nums[minIdx]
        return nums
```

[返回目录](#503)

---

### 归并排序
#### 题目描述
归并排序给定数组。
#### Python Solution：
**分析：** 大问题分解成小问题，再对有序的小问题进行合并，节省性能。

```Python
class Solution:
    def mergeSort(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            res = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res += left[i:] or right[j:]
            return res

        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return merge(left, right)
```

[返回目录](#504)

---

### 快速排序
#### 题目描述
快速排序给定数组。
#### Python Solution：
**分析：** 第一种可以清晰地看出来思维，但是额外空间很多，所以推荐用这种讲思路，再用第二种方法优化空间复杂度和代码。

```Python
class Solution:
    def quickSort(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        pivot = random.choice(nums)
        left = [v for v in nums if v < pivot]
        mid = [v for v in nums if v == pivot]
        right = [v for v in nums if v > pivot]
        return self.quickSort(left) + mid + self.quickSort(right)
```

**优化：**

```Python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, lower, upper):
        if lower < upper:
            pivot = self.partition(nums, lower, upper)
            self.quicksort(nums, lower, pivot - 1)
            self.quicksort(nums, pivot + 1, upper)
        else:
            return

    def partition(self, nums, lower, upper):

        pivot = nums[upper]

        i = lower

        for j in range(lower, upper):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[upper] = nums[upper], nums[i]

        return i
```

[返回目录](#505)

---

### 堆排序
#### 题目描述
堆排序给定数组。
#### Python Solution：
**分析：**

```Python
class Solution:
    def heapSort(self, nums: List[int]) -> List[int]:
        import heapq
        res = []
        heapq.heapify(nums)

        for i in range(len(nums)):
            res.append(heapq.heappop(nums))
        return res
```

```Python
class Solution:
    def sortArray(self, nums):
        def heapify(nums, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and nums[i] < nums[l]:
                largest = l

            if r < n and nums[largest] < nums[r]:
                largest = r

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]

                heapify(nums, n, largest)

        n = len(nums)

        for i in range(n, -1, -1):
            heapify(nums, n, i)

        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)

        return nums
```

```Python
class Solution:
    # 大根堆（从小到大排列）
    def sortArray(self, nums):
        # 调整堆
        def adjustHeap(nums, i, size):
            # 非叶子结点的左右两个孩子
            lchild = 2 * i + 1
            rchild = 2 * i + 2
            # 在当前结点、左孩子、右孩子中找到最大元素的索引
            largest = i
            if lchild < size and nums[lchild] > nums[largest]:
                largest = lchild
            if rchild < size and nums[rchild] > nums[largest]:
                largest = rchild
            # 如果最大元素的索引不是当前结点，把大的结点交换到上面，继续调整堆
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                # 第 2 个参数传入 largest 的索引是交换前大数字对应的索引
                # 交换后该索引对应的是小数字，应该把该小数字向下调整
                adjustHeap(nums, largest, size)
        # 建立堆
        def builtHeap(nums, size):
            for i in range(len(nums)//2)[::-1]: # 从倒数第一个非叶子结点开始建立大根堆
                adjustHeap(nums, i, size) # 对所有非叶子结点进行堆的调整
            # print(nums)  # 第一次建立好的大根堆
        # 堆排序
        size = len(nums)
        builtHeap(nums, size)
        for i in range(len(nums))[::-1]:
            # 每次根结点都是最大的数，最大数放到后面
            nums[0], nums[i] = nums[i], nums[0]
            # 交换完后还需要继续调整堆，只需调整根节点，此时数组的 size 不包括已经排序好的数
            adjustHeap(nums, 0, i)
        return nums  # 由于每次大的都会放到后面，因此最后的 nums 是从小到大排列
```

[返回目录](#506)

---

### 计数排序
#### 题目描述
计数排序给定数组。
#### Python Solution：
**分析：** 要求数组中元素必须大于 0 ，不然需要额外操作：桶的数量调整为最大值减最小值的差值个。最后加和成结果的时候需要减掉最小值。适合重复数量多而且数据较集中的排序。

```Python
class Solution:
    def countingSort(nums):
        bucket = [0] * (max(nums) + 1) # 桶的个数
        for num in nums:  # 将元素值作为键值存储在桶中，记录其出现的次数
            bucket[num] += 1
        i = 0  # nums 的索引
        for j in range(len(bucket)):
            while bucket[j] > 0:
                nums[i] = j
                bucket[j] -= 1
                i += 1
        return nums
```

[返回目录](#507)

---

### 桶排序
#### 题目描述
桶排序给定数组。
#### Python Solution：
**分析：**

```Python
class Solution:
  def bucketSort(nums, defaultBucketSize = 5):
      maxVal, minVal = max(nums), min(nums)
      bucketSize = defaultBucketSize  # 如果没有指定桶的大小，则默认为5
      bucketCount = (maxVal - minVal) // bucketSize + 1  # 数据分为 bucketCount 组
      buckets = [[] for _ in range(bucketSize)]
      # 利用函数映射将各个数据放入对应的桶中
      for num in nums:
          buckets[(num - minVal) // bucketSize].append(num)
      nums.clear()  # 清空 nums
      # 对每一个二维桶中的元素进行排序
      for bucket in buckets:
          insertionSort(bucket)  # 假设使用插入排序
          nums.extend(bucket)    # 将排序好的桶依次放入到 nums 中
      return nums
```

[返回目录](#501)

---

### 冒泡排序
#### 题目描述
冒泡排序给定数组。
#### Python Solution：
**分析：**

```Python

```

[返回目录](#501)

---


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

### 冒泡排序
#### 题目描述
冒泡排序给定数组。
#### Python Solution：
**分析：**

```Python

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

### 冒泡排序
#### 题目描述
冒泡排序给定数组。
#### Python Solution：
**分析：**

```Python

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

### 冒泡排序
#### 题目描述
冒泡排序给定数组。
#### Python Solution：
**分析：**

```Python

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

### 冒泡排序
#### 题目描述
冒泡排序给定数组。
#### Python Solution：
**分析：**

```Python

```

[返回目录](#501)

---

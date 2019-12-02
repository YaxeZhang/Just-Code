<span id = "00"></span>
## 基础		
 - [27	Remove Element]
 - [26	Remove Duplicates from Sorted Array]
 - [80	Remove Duplicates from Sorted Array II]
 - [277	Find the Celebrity]
 - [189. Rotate Array](#189-rotate-array)
 - [41. First Missing Positive](#41-first-missing-positive)
 - [299	Bulls and Cows]
 - [134	Gas Station]
 - [118. Pascal's Triangle](#118-pascals-triangle)
 - [119. Pascal's Triangle II](#119-pascals-triangle-ii)
 - [169	Majority Element]
 - [229	Majority Element II]
 - [274	H-Index]
 - [275	H-Index II	Binary Search]
 - [243	Shortest Word Distance]
 - [244	Shortest Word Distance II]
 - [245	Shortest Word Distance III]
 - [217. Contains Duplicate](#217-contains-duplicate)
 - [219. Contains Duplicate II](#219-contains-duplicate-ii)
 - [220. Contains Duplicate III](#220-contains-duplicate-iii)
 - [55	Jump Game]
 - [45	Jump Game II]
 - [11	Container With Most Water]
 - [42. Trapping Rain Water](#42-trapping-rain-water)
 - [334	Increasing Triplet Subsequence]
 - [128	Longest Consecutive Sequence]
 - [164	Maximum Gap	Bucket]
 - [287	Find the Duplicate Number]
 - [135	Candy]
 - [330	Patching Array]
 - [78. Subsets](#78-subsets)
 - [763. Partition Labels](#763-partition-labels)
## 提高		
 - [4	Median of Two Sorted Arrays]
 - [321	Create Maximum Number]
 - [327	Count of Range Sum]
 - [289. Game of Life](#289-game-of-life)
## Interval		
 - [57. Insert Interval](#57-insert-interval)
 - [56. Merge Intervals](#56-merge-intervals)
 - [986. Interval List Intersections](#986-interval-list-intersections)
 - [252	Meeting Rooms]
 - [253	Meeting Rooms II]
 - [352	Data Stream as Disjoint Intervals]
## Counter		
 - [239. Sliding Window Maximum](#239-sliding-window-maximum)
 - [295. Find Median from Data Stream](#295-find-median-from-data-stream)
 - [325	Maximum Size Subarray Sum Equals k]
 - [209. Minimum Size Subarray Sum](#209-minimum-size-subarray-sum)
 - [795. Number of Subarrays with Bounded Maximum](#795-number-of-subarrays-with-bounded-maximum)
 - [238. Product of Array Except Self](#238-product-of-array-except-self)
 - [152. Maximum Product Subarray](#152-maximum-product-subarray)
 - [228	Summary Ranges]
 - [163	Missing Ranges]
## Sort		
 - [88. Merge Sorted Array](#88-merge-sorted-array)
 - [75. Sort Colors](#75-sort-colors)
 - [283. Move Zeroes](#283-move-zeroes)
 - [376	Wiggle Subsequence]
 - [280	Wiggle Sort]
 - [324	Wiggle Sort II]

## 189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

给定一个数组，将数组向右旋转k步，其中k为非负数。

**Example:1**

```
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example:2**

```
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

---

### Python Solution
**分析：** 可以用 Python 的列表的交换做，也可以通过翻转来做，推荐第二种Solution

**Solution 1:**

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k == 0:return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
```

**Solution 2:**

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        k %= len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
```

[返回目录](#00)

## 41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

给定未排序的整数数组，找到最小的缺失正整数。

**Example:1**

```
Input: [3,4,-1,1]
Output: 2
```

**Example:2**

```
Input: [1,2,0]
Output: 3
```

---

### Python Solution
**分析：** Hard 难度的题目，但是思路很简单：就是把 1 到 len(nums) 的数放到对应下标（即减一）的位置，然后从头遍历，找到第一个不满足条件的值。

```python
class Solution:
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 0 <= nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
        return len(nums) + 1
```

[返回目录](#00)

## 118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

给定一个非负整数numRows，生成Pascal三角形的第一个numRows。

**Example:1**

```
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

---

### Python Solution
**分析：** 杨辉三角,注意条件即可.

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res += [[1] + [res[-1][i] + res[-1][i + 1] for i in range(len(res[-1]) - 1)] + [1]]
        return res
```

[返回目录](#00)

## 119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

给定非负索引k（其中k≤33），返回Pascal三角形的第k个索引行。

**Example:1**

```
Input: 3
Output: [1,3,3,1]
```

---

### Python Solution
**分析：** 杨辉三角的第 k 层,注意条件空间 O(k) ,所以我们要先构造好 res 。

```python
class Solution:
    def getRow(self, rowIndex):
        res = [1] * (rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                res[j] += res[j-1]
        return res
```

[返回目录](#00)

## 217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

给定一个整数数组，查找数组是否包含任何重复项。 如果数组中任何值至少出现两次，则函数应返回true，如果每个元素都不相同，则返回false。

**Example:1**

```
Input: [1,2,3,1]
Output: true
```

**Example:2**

```
Input: [1,2,3,4]
Output: false
```

---

### Python Solution
**分析：** 用 set 作 hash 表，如果存在重复的元素，则 set 的长度一定小于 nums 的长度。

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
```

[返回目录](#00)

## 219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

给定一个整数数组和一个整数k，找出数组中是否存在两个不同的索引i和j，使得nums [i] = nums [j]并且i和j之间的绝对差值最多为k。

**Example:1**

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example:2**

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

---

### Python Solution
**分析：** 建立哈希表，存储距离最近的上一次索引，判断距离，如果满足条件了将 flag 设为 True ，否则不满足返回 flag = Flase 。

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        used = {}
        flag = False
        for i, v in enumerate(nums):
            if v in used and not flag:
                flag = (i - used[v] <= k)
            used[v] = i
        return flag
```

[返回目录](#00)

## 220. Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

给定一个整数数组，请找出数组中是否存在两个不同的索引i和j，以使 nums[i] 和 nums[j] 之间的绝对差最大为 t，并且i和j之间的绝对差最大为 k

**Example:1**

```
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```

**Example:2**

```
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```

---

### Python Solution
**分析：** 暴力法加了个判断效率还奇高？

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(nums) == len(set(nums)): return False
        for i in range(len(nums)):
            for j in range(1, k + 1):
                if i + j >= len(nums): break
                if abs(nums[i] - nums[i + j]) <= t: return True
        return False
```

[返回目录](#00)

## 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

给定n个代表海拔图的非负整数，其中每个条的宽度为1，计算下雨后它能捕获多少水。

**Example:1**

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

---

### Python Solution
**分析：** 双指针做法，左右贪心。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res, i, j = 0, 0, len(height)-1
        l_max, r_max = height[i], height[j]
        while i < j:
            if l_max > r_max:
                j -= 1
                r_max = max(r_max, height[j])
                res += max(0, r_max - height[j])
            else:
                i += 1
                l_max = max(l_max, height[i])
                res += max(0, l_max - height[i])
        return res
```

[返回目录](#00)

## 78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

给定一组不同的整数nums，返回所有可能的子集（幂集）。 注意：解决方案集不得包含重复的子集。

**Example:1**

```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

---

### Python Solution
**分析：**

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets]
        return subsets

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda subsets, n: subsets + [s + [n] for s in subsets], nums, [[]])
```

[返回目录](#00)

## 763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

给出一个小写字母的字符串S。我们希望将此字符串分成尽可能多的部分，以便每个字母最多显示一个部分，并返回代表这些部分大小的整数列表。

**Example:1**

```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

---

### Python Solution
**分析：** 字典推导式也很很很厉害。两边遍历，很巧妙。

```python
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans
```

[返回目录](#00)

## 289. Game of Life

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

给定一个包含m x n个单元的板，每个单元的初始状态为活动（1）或无效（0）。每个单元使用以下四个规则（取自以上Wikipedia文章）与其八个邻居（水平，垂直，对角线）进行交互：

少于两个活动邻居的任何活动单元都会死亡，好像是由人口不足造成的。任何有两个或三个活邻居的活细胞都可以存活到下一代。任何具有三个以上活邻居的活细胞都会死亡，好像是由于人口过多而死。任何具有三个活邻居的死细胞都将变成活细胞，就像通过繁殖一样。

编写一个函数，以根据给定的当前状态计算板的下一个状态（一次更新后）。通过将上述规则同时应用于当前状态下的每个单元格来创建下一个状态，在该单元格中，生死同时发生。

**Example:1**

```
Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
```

---

### Python Solution
**分析：** 原地 O(1) 的点在于时间换空间，两边遍历，第一遍标状态，第二遍校正。

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        delta = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                count = 0
                for dx, dy in delta:
                    if 0 <= x+dx < m and 0 <= y+dy < n and board[x+dx][y+dy] > 0:
                        count += 1
                if board[x][y] == 1:
                    if count not in (2, 3):
                        board[x][y] = 2
                else:
                    if count == 3:
                        board[x][y] = -1
        for x in range(m):
            for y in range(n):
                if board[x][y] == -1:
                    board[x][y] = 1
                elif board[x][y] == 2:
                    board[x][y] = 0
```

[返回目录](#00)

## 57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

给定一组非重叠区间，在区间中插入新区间（必要时合并）。 您可以假设区间最初是根据其下限排序的。

**Example**

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

---

### Python Solution
**分析：** 虽然这是一道 Hard 难度的题，但其实并没有难度。Talk is cheap, show you the code.

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        left, right = [], []
        for i in intervals:
            if i[1] < start:
                left += i,
            elif i[0] > end:
                right += i,
            else:
                start = min(start, i[0])
                end = max(end, i[1])
        return left + [[start, end]] + right
```

[返回目录](#00)

## 56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

给定包含一些区间的集合，合并所有重叠的区间。

**Example**

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

---

### Python Solution
**分析：** 先根据区间下限对给定的区间集合进行排序，然后逐个区间与 res 中存在的最后一个区间进行比较。如果没有交集，则将新的区间存入 res 作为新的最后一个区间；如果有交集，则将最后一个区间的上限更新为更大的那个上限。

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res += i,
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res
```

**优化** 在 LeetCode 上提交发现 Runtime 较低，应该是每次都对 res 进行读取的原因，所以我们设置两个变量来降低读取 res 的频率。但是它带来的问题就是需要判断区间集合是否为空。

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x : x[0])
        res = []
        l, r = intervals[0]
        for i in range(1, len(intervals)):
            il, ir = intervals[i]
            if r < il:
                res += [l, r],
                l, r = il, ir
            else:
                r = max(r, ir)
        res += [l, r],
        return res
```

[返回目录](#00)

## 986. Interval List Intersections

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

给定两个闭合间隔列表，每个间隔列表是成对不相交的并且按排序顺序。 返回这两个间隔列表的交集。 （形式上，闭区间[a，b]（a <= b）表示实数x的集合，其中a <= x <= b。两个闭区间的交集是一组空的实数 或者可以表示为闭区间。例如，[1,3]和[2,4]的交集是[2,3]。）

**Example**

```
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
```

---

### Python Solution
**分析：** 双指针进行比对，如果有交集则在 res 中添加。移动拥有更小末尾的指针，进行判断下一个区间和当前较大末尾的区间是否有交集。

```python
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            if b2 >= a1 and a2 >= b1:
                res += [max(a1, b1), min(a2, b2)],
            if a2 < b2: i += 1
            else: j += 1
        return res
```

[返回目录](#00)

## 239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

给定一个数组nums，有一个大小为k的滑动窗口，它从数组的最左边移动到最右边。 您只能在窗口中看到k编号。 每次滑动窗口向右移动一个位置。 返回最大滑动窗口。

**Example**

```
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

---

### Python Solution
**分析：**

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        res = []
        for i, v in enumerate(nums):
            while dq and nums[dq[-1]] < v:
                dq.pop()
            dq += i,
            if dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                res += nums[dq[0]],
        return res
```

[返回目录](#00)

## 295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

中位数是有序整数列表中的中间值。 如果列表的大小是偶数，则没有中间值。 因此，中位数是两个中间值的平均值。

**Example**

```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
```

---

### Python Solution
**分析：** 维护一个最大堆、一个最小堆，所以插入的时间是 O(lgn), 找到中位数的时间是 O(1)。

```python
from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
```

[返回目录](#00)

## 209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

给定n个正整数和正整数s的数组，找到连续子阵列的最小长度，其总和≥s。 如果没有，则返回0。

**Example**

```
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```

---

### Python Solution
**分析：** 滑动窗口的思路，窗口的右端每右移一位就进行判断，如果总和大于等于 s ，则将滑动窗口的左端向右移动到满足条件的最边界位置，当前的窗口长度与最小长度进行比较更新。

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, sum, res = 0, 0, float('inf')
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= s:
                i, sum, res = i + 1, sum - nums[i], min(res, j - i + 1)
        return 0 if res == float('inf') else res
```

[返回目录](#00)

## 795. Number of Subarrays with Bounded Maximum

We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

给定一个正整数数组A，以及两个正整数L和R（L <= R）。 返回（连续的，非空的）子数组的数量，以使该子数组中最大数组元素的值至少为L，最多为R。

**Example**

```
Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
```

---

### Python Solution
**分析：** 这道题不在前 400 道里，但我觉得比较经典，可以研究一下。利用 dp 来标记状态，利用 prev 来标记左边界，当碰到第一个满足条件的数的时候，dp = i-prev 即为向左扩张，后面的每次加的 dp 其实就是向右扩张右边界，想通了以后十分顺畅。

```python
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        res = dp = 0
        prev = -1
        for i, v in enumerate(A):
            if v > R:
                dp = 0
                prev = i
            elif L <= v <= R:
                dp = i - prev
            res += dp
        return res
```

[返回目录](#00)

## 238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

给定一个由n个整数组成的数组num，其中n> 1，则返回一个数组输出，使得output [i]等于除nums [i]之外所有nums元素的乘积。

**Example**

```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```

**Note:**

注意：请不用除法并在O（n）中求解。 跟进：您能以恒定的空间复杂度解决它吗？ （出于空间复杂度分析的目的，输出数组不算作额外的空间。）

---

### Python Solution
**分析：** 剑指 offer 里一样的题目，重点在于分解步骤，左边乘积乘以 1 乘以右边乘积。

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        tmp = 1
        for j in range(len(nums)-2, -1, -1):
            tmp *= nums[j+1]
            res[j] *= tmp
        return res
```

[返回目录](#00)

## 152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

给定一个整数数组nums，查找具有最大乘积的数组（至少包含一个数字）中的连续子数组。

**Example**

```
Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

---

### Python Solution
**分析：** A 是前缀乘积，B 是后缀乘积。找到最大的那个就可以了。很巧妙的解法。

```python
class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)
```

[返回目录](#00)

## 88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

给定两个排序的整数数组nums1和nums2，将nums2合并为nums1作为一个排序的数组。。

**Example**

```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
```

---

### Python Solution
**分析：** 从尾部进行数组的比较和填充不会移动之前的元素，比较高效。最后确保 nums2 中的元素全部移到了 nums1 中，因为 nums2 的前几个元素可能比 nums1 的第一个元素都小。

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
```

[返回目录](#00)

## 75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

给定一个具有红色，白色或蓝色的n个对象的数组，对它们进行就地排序，使相同颜色的对象相邻，颜色顺序为红色，白色和蓝色。

这里，我们将使用整数0,1和2分别表示红色，白色和蓝色。

**Example**

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

---

### Python Solution
**分析：** 三路快排的思想，用三个指针，但是只关注左边 0 的位置和右边 2 的位置即可，排序交换完结果肯定中键都是 1 。

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = i = 0
        two = len(nums)
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
```

[返回目录](#00)

## 283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

给定一个数组nums，写一个函数将所有0移动到它的末尾，同时保持非零元素的相对顺序。

**Example**

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

---

### Python Solution
**分析：** k 永远指向的是遍历到的交换后最开头的一个 0 ，并且与当前遍历到的不为 0 的数进行交换。当遍历到最后的时候，即完成了所有的交换，将所有 0 交换到了末尾。

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i]:
                if i != k:
                    nums[i], nums[k] = nums[k], nums[i]
                k += 1
```

[返回目录](#00)

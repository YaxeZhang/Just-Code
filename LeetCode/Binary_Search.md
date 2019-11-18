<span id = "00"></span>
## 基础
 - [278. First Bad Version](#278-first-bad-version)
 - [35. Search Insert Position](#35-search-insert-position)
 - [33. Search in Rotated Sorted Array](#33-search-in-rotated-sorted-array)
 - [81	Search in Rotated Sorted Array II]
 - [153. Find Minimum in Rotated Sorted Array](#153-find-minimum-in-rotated-sorted-array)
 - [154. Find Minimum in Rotated Sorted Array II](#154-find-minimum-in-rotated-sorted-array-ii)
 - [162. Find Peak Element](#162-find-peak-element)
 - [374. Guess Number Higher or Lower](#374-guess-number-higher-or-lower)
 - [34. Find First and Last Position of Element in Sorted Array](#34-find-first-and-last-position-of-element-in-sorted-array)
 - [315. Count of Smaller Numbers After Self](#315-count-of-smaller-numbers-after-self)
 - [300. Longest Increasing Subsequence](#300-longest-increasing-subsequence)
 - [354	Russian Doll Envelopes]
 - [540. Single Element in a Sorted Array](#540-single-element-in-a-sorted-array)


## 278. First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

您是产品经理，目前正在领导团队开发新产品。 不幸的是，您产品的最新版本未通过质量检查。 由于每个版本都是基于先前版本开发的，因此错误版本之后的所有版本也都是错误的。 假设您有n个版本[1、2，...，n]，并且想要找出第一个不良版本，这将导致随后的所有不良版本。 您将获得一个API bool isBadVersion（version），它将返回版本是否错误。 实现一个功能以查找第一个错误的版本。 您应该减少对API的调用次数。

**Example**

```
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
```

---

### Python Solution
**分析：**

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
```

[返回目录](#00)

## 35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

给定排序数组和目标值，如果找到目标，则返回索引。如果不是，则返回按顺序插入索引的位置的索引。 您可以假设阵列中没有重复项。

**Example**

```
Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
```

---

### Python Solution
**分析：** 很经典的 cpp 标准库里二分法的写法，推荐研读一下 lower_bound() 和 upper_bound()。这里要注意的点是 high 要设置为 len(nums) 的原因是像第三个例子会超出数组的最大值，所以要让 lo 能到 这个下标。

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:        
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
```

[返回目录](#00)

## 33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

假设以升序排序的数组在事先未知的某个轴上旋转。 （即[0,1,2,4,5,6,7]可能会变成[4,5,6,7,0,1,2]）。 将为您提供要搜索的目标值。 如果在数组中找到，则返回其索引，否则返回-1。 您可以假设数组中不存在重复项。 您算法的运行时复杂度必须为O（logn）的顺序。

**Example**

```
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

---

### Python Solution
**分析：** 这里的灵魂是三个异或。

```python
class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if lo == hi and target == nums[lo] else -1
```

[返回目录](#00)

## 153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

假设以升序排序的数组在事先未知的某个轴上旋转。 （即[0,1,2,4,5,6,7]可能变为[4,5,6,7,0,1,2]）。 找到最小的元素。 您可以假设数组中不存在重复项。

**Example**

```
Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
```

---

### Python Solution
**分析：**

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
```

[返回目录](#00)

## 154. Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.

假设以升序排序的数组在事先未知的某个轴上旋转。 （即[0,1,2,4,5,6,7]可能变为[4,5,6,7,0,1,2]）。 找到最小的元素。 该数组可能包含重复项。

**Example**

```
Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0
```

---

### Python Solution
**分析：** 和上一道的区别在于上一题没有重复项，这一道要加个条件来解决重复项的问题，最差程度是 O(n) 。

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] == nums[hi]:
                hi -= 1
            else:
                hi = mid
        return nums[lo]
```

[返回目录](#00)

## 162. Find Peak Element

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

峰值元素是大于其相邻元素的元素。 给定一个输入数组nums，其中nums [i]≠nums [i + 1]，找到一个峰值元素并返回其索引。 该数组可能包含多个峰，在这种情况下，将索引返回到任何一个峰都可以。 您可能会想到nums [-1] = nums [n] =-∞。

**Example**

```
Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
```

---

### Python Solution
**分析：**

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
```

[返回目录](#00)

## 374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

我们正在玩猜猜游戏。游戏如下： 我选择一个从1到n的数字。您必须猜测我选了哪个号码。 每次您猜错了，我都会告诉您数字是高还是低。

**Example**

```
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
```

---

### Python Solution
**分析：**

```python
class Solution(object):
    def guessNumber(self, n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) / 2
            lo, hi = ((mid, mid), (mid+1, hi), (lo, mid-1))[guess(mid)]
        return lo
```

[返回目录](#00)

## 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

给定一个以升序排列的整数nums数组，请找到给定目标值的开始和结束位置。 算法的运行时复杂度必须为O（log n）的量级。 如果在数组中找不到目标，则返回[-1，-1]。

**Example**

```
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

---

### Python Solution
**分析：** O(nlgn) 的时间复杂度，十分巧妙。

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) // 2
                l, r = search(lo, mid), search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums)-1)
```

[返回目录](#00)

## 315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

您将得到一个整数数组nums，并且必须返回一个新的counts数组。 counts数组具有以下属性：counts [i]是nums [i]右侧较小元素的数量。

**Example**

```
Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```

---

### Python Solution
**分析：** 本题考察的是二分搜索，两种解法，一种是用 python 的库，另一种是自己构造二分搜索函数。这道题的拓展很多，更推荐的做法是二分搜索树或者线段树。

```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res, sortedNums = [], []
        for num in nums[::-1]:
            i = bisect.bisect_left(sortedNums, num)
            res.append(i)
            sortedNums[i:i] = num,

        return res[::-1]
```

```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        tmp = []

        def binsrh(tmp, target):
            if not tmp:
                tmp.append(target)
                return 0
            if target > tmp[-1]:
                tmp.append(target)
                return len(tmp) - 1
            if target < tmp[0]:
                tmp[0:0] = [target]
                return 0
            i, j = 0, len(tmp) - 1
            while i < j:
                mid = (i + j) // 2
                if tmp[mid] >= target:
                    j = mid
                else:
                    i = mid + 1
            tmp[i:i] = [target]
            return i

        return [binsrh(tmp, nums[i]) for i in range(len(nums)-1, -1, -1)][::-1]
        return tmp
```

[返回目录](#00)

## 300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

给定一个未排序的整数数组，请找到最长递增子序列的长度。

**Example**

```
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

---

### Python Solution
**分析：** 非常精彩的题目，常规动态规划解法是 O(n^2) 的时间复杂度，但是用二分搜索可以减少到 O(nlgn)，尤其是迭代更新的部分需要好好品味下。

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(1, i+1):
                if nums[i] > nums[i-j]:
                    dp[i] = max(dp[i], dp[i-j]+1)
        return max(dp) if dp else 0
```

**O(nlgn)的解法**

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        dp = [nums[0]]
        for n in nums[1:]:
            if n > dp[-1]:
                dp.append(n)
            else:
                left,right = 0, len(dp)
                while left < right:
                    mid = left + (right-left)//2
                    if dp[mid] < n:
                        left = mid + 1
                    else:
                        right = mid
                dp[left] = n
        return len(dp)
```

[返回目录](#00)

## 540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

您将获得一个仅由整数组成的排序数组，其中每个元素精确出现两次，但一个元素仅出现一次。 找到只出现一次的单个元素。

**Example**

```
Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
```

---

### Python Solution
**分析：** 异或的巧妙应用！

```python
class Solution:
    def singleNonDuplicate(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
```

[返回目录](#00)

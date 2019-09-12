<span id = "00"></span>
## 基础		
 - [27	Remove Element]
 - [26	Remove Duplicates from Sorted Array]
 - [80	Remove Duplicates from Sorted Array II]
 - [277	Find the Celebrity]
 - [189	Rotate Array]
 - [41	First Missing Positive]
 - [299	Bulls and Cows]
 - [134	Gas Station]
 - [118	Pascal's Triangle]
 - [119	Pascal's Triangle II]
 - [169	Majority Element]
 - [229	Majority Element II]
 - [274	H-Index]
 - [275	H-Index II	Binary Search]
 - [243	Shortest Word Distance]
 - [244	Shortest Word Distance II]
 - [245	Shortest Word Distance III]
 - [217. Contains Duplicate](#217-contains-duplicate)
 - [219. Contains Duplicate II](#219-contains-duplicate-ii)
 - [220	Contains Duplicate III]
 - [55	Jump Game]
 - [45	Jump Game II]
 - [121	Best Time to Buy and Sell Stock]
 - [122	Best Time to Buy and Sell Stock II]
 - [123	Best Time to Buy and Sell Stock III]
 - [188	Best Time to Buy and Sell Stock IV]
 - [309	Best Time to Buy and Sell Stock with Cooldown]
 - [11	Container With Most Water]
 - [42	Trapping Rain Water]
 - [334	Increasing Triplet Subsequence]
 - [128	Longest Consecutive Sequence]
 - [164	Maximum Gap	Bucket]
 - [287	Find the Duplicate Number]
 - [135	Candy]
 - [330	Patching Array]
## 提高		
 - [4	Median of Two Sorted Arrays]
 - [321	Create Maximum Number]
 - [327	Count of Range Sum]
 - [289	Game of Life]
## Interval		
 - [57	Insert Interval]
 - [56	Merge Intervals]
 - [252	Meeting Rooms]
 - [253	Meeting Rooms II]
 - [352	Data Stream as Disjoint Intervals]
## Counter		
 - [239. Sliding Window Maximum](#239-sliding-window-maximum)
 - [295	Find Median from Data Stream]
 - [53	Maximum Subarray]
 - [325	Maximum Size Subarray Sum Equals k]
 - [209. Minimum Size Subarray Sum](#209-minimum-size-subarray-sum)
 - [238	Product of Array Except Self]
 - [152	Maximum Product Subarray]
 - [228	Summary Ranges]
 - [163	Missing Ranges]
## Sort		
 - [88	Merge Sorted Array]
 - [75	Sort Colors]
 - [283. Move Zeroes](#283-move-zeroes)
 - [376	Wiggle Subsequence]
 - [280	Wiggle Sort]
 - [324	Wiggle Sort II]

## 217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

给定一个整数数组，查找数组是否包含任何重复项。 如果数组中任何值至少出现两次，则函数应返回true，如果每个元素都不相同，则返回false。

**Example:1**

> Input: [1,2,3,1]
> Output: true

**Example:2**

> Input: [1,2,3,4]
> Output: false

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

> Input: nums = [1,2,3,1], k = 3
> Output: true

**Example:2**

> Input: nums = [1,2,3,1,2,3], k = 2
> Output: false

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

## 209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

给定n个正整数和正整数s的数组，找到连续子阵列的最小长度，其总和≥s。 如果没有，则返回0。

**Example**

> Input: s = 7, nums = [2,3,1,2,4,3]
> Output: 2
> Explanation: the subarray [4,3] has the minimal length under the problem constraint.
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

## 283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

给定一个数组nums，写一个函数将所有0移动到它的末尾，同时保持非零元素的相对顺序。

**Example**

> Input: [0,1,0,3,12]
> Output: [1,3,12,0,0]

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

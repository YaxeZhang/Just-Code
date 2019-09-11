<span id = "00"></span>
## 基础		
27	Remove Element
26	Remove Duplicates from Sorted Array
80	Remove Duplicates from Sorted Array II
277	Find the Celebrity
189	Rotate Array
41	First Missing Positive
299	Bulls and Cows
134	Gas Station
118	Pascal's Triangle
119	Pascal's Triangle II
169	Majority Element
229	Majority Element II
274	H-Index
275	H-Index II	Binary Search
243	Shortest Word Distance
244	Shortest Word Distance II
245	Shortest Word Distance III
217	Contains Duplicate
219	Contains Duplicate II
220	Contains Duplicate III
55	Jump Game
45	Jump Game II
121	Best Time to Buy and Sell Stock
122	Best Time to Buy and Sell Stock II
123	Best Time to Buy and Sell Stock III
188	Best Time to Buy and Sell Stock IV
309	Best Time to Buy and Sell Stock with Cooldown
11	Container With Most Water
42	Trapping Rain Water
334	Increasing Triplet Subsequence
128	Longest Consecutive Sequence
164	Maximum Gap	Bucket
287	Find the Duplicate Number
135	Candy
330	Patching Array
## 提高		
4	Median of Two Sorted Arrays
321	Create Maximum Number
327	Count of Range Sum
289	Game of Life
## Interval		
57	Insert Interval
56	Merge Intervals
252	Meeting Rooms
253	Meeting Rooms II
352	Data Stream as Disjoint Intervals
## Counter		
239	Sliding Window Maximum
295	Find Median from Data Stream
53	Maximum Subarray
325	Maximum Size Subarray Sum Equals k
209	Minimum Size Subarray Sum
238	Product of Array Except Self
152	Maximum Product Subarray
228	Summary Ranges
163	Missing Ranges
## Sort		
88	Merge Sorted Array
75	Sort Colors
 - [283. Move Zeroes](283-move-zeroes)
376	Wiggle Subsequence
280	Wiggle Sort
324	Wiggle Sort II


## 283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

给定一个数组nums，写一个函数将所有0移动到它的末尾，同时保持非零元素的相对顺序。

**Example**

> Input: [0,1,0,3,12]
> Output: [1,3,12,0,0]

---

### Python Solution
**分析：**

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

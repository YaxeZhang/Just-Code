<span id = "00"></span>
## 基础		
7	Reverse Integer
165	Compare Version Numbers
66	Plus One
8	String to Integer (atoi)
258	Add Digits
67	Add Binary
43	Multiply Strings
29	Divide Two Integers
69	Sqrt(x)
50	Pow(x, n)
367	Valid Perfect Square
365	Water and Jug Problem
204	Count Primes
## Sum		
1	Two Sum
 - [167. Two Sum II](167-two-sum-ii)
15	3Sum
16	3Sum Closest
259	3Sum Smaller
18	4Sum
## 很少考		
231	Power of Two
326	Power of Three
342	Power of Four
372	Super Pow
233	Number of Digit One
319	Bulb Switcher
292	Nim Game
202	Happy Number
400	Nth Digit
263	Ugly Number
264	Ugly Number II
306	Additive Number
172	Factorial Trailing Zeroes
343	Integer Break
396	Rotate Function
390	Elimination Game
386	Lexicographical Numbers
357	Count Numbers with Unique Digits
360	Sort Transformed Array
397	Integer Replacement
368	Largest Divisible Subset


## 167. Two Sum II

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

给定已按升序排序的整数数组，找到两个数字，使它们相加到特定的目标数。
函数twoSum应返回两个数字的索引，以便它们加起来到目标，其中index1必须小于index2。

**Example**

> Input: numbers = [2,7,11,15], target = 9
> Output: [1,2]
> Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

---

### Python Solution
**分析：**

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0,len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return i + 1, j + 1
```

[返回目录](#00)

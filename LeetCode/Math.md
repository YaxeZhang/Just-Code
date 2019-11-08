<span id = "00"></span>
## 基础		
 - [7. Reverse Integer](#7-reverse-integer)
 - [165	Compare Version Numbers]
 - [66. Plus One](#66-plus-one)
 - [8	String to Integer (atoi)]
 - [258	Add Digits]
 - [67	Add Binary]
 - [43	Multiply Strings]
 - [29	Divide Two Integers]
 - [69. Sqrt(x)](#69-sqrt-x-)
 - [50. Pow(x, n)](#50-pow-x--n-)
 - [367	Valid Perfect Square]
 - [365	Water and Jug Problem]
 - [204. Count Primes](204-count-primes)
## Sum		
 - [1	Two Sum]
 - [167. Two Sum II](#167-two-sum-ii)
 - [15	3Sum]
 - [16	3Sum Closest]
 - [259	3Sum Smaller]
 - [18	4Sum]
 - [611. Valid Triangle Number](#611-valid-triangle-number)
## 很少考		
 - [231	Power of Two]
 - [326	Power of Three]
 - [342	Power of Four]
 - [372	Super Pow]
 - [233	Number of Digit One]
 - [319	Bulb Switcher]
 - [292	Nim Game]
 - [202. Happy Number](#202-happy-number)
 - [400	Nth Digit]
 - [263. Ugly Number](#263-ugly-number)
 - [264. Ugly Number II](#264-ugly-number-ii)
 - [306	Additive Number]
 - [172	Factorial Trailing Zeroes]
 - [343. Integer Break](#343-integer-break)
 - [396	Rotate Function]
 - [390	Elimination Game]
 - [386	Lexicographical Numbers]
 - [357. Count Numbers with Unique Digits](#357-count-numbers-with-unique-digits)
 - [360	Sort Transformed Array]
 - [397	Integer Replacement]
 - [368	Largest Divisible Subset]

## 7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

给定一个32位带符号整数，整数的倒置的数字。

**Example:1**

```
Input: -123
Output: -321

Input: 120
Output: 21
```

---

### Python Solution
**分析：** 考查的是数学解法而不是 int 转 str 倒置。

```python
class Solution:
    def reverse(self, x):
        result = 0

        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1

        while x:
            result = result * 10 + x % 10
            x //= 10

        return 0 if result > pow(2, 31) else result * symbol
```

[返回目录](#00)

## 66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

给定表示非负整数的非空数字数组，加上整数的1。

存储数字使得最高有效数字位于列表的开头，并且数组中的每个元素包含单个数字。

您可以假设整数不包含任何前导零，除了数字0本身。

**Example:1**

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

**Example:2**

```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

---

### Python Solution
**分析：** 从后往前找到第一位不为 9 的数字加一返回数组即可，如果为 9 ，将这一位置 0 ，继续向前寻找。如果都为 9 ，则在数组头部插入 1 。

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        digits.insert(0, 1)
        return digits
```

[返回目录](#00)

## 69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

实现int sqrt（int x）。 计算并返回x的平方根，其中x保证为非负整数。 由于返回类型是整数，因此十进制数字将被截断，并且仅返回结果的整数部分。

**Example:1**

```
Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
```

---

### Python Solution
**分析：** 两种方法，一种是二分法，一种是牛顿迭代法。

```python
class Solution:
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1
```

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = (r + x//r) // 2
        return r
```

[返回目录](#00)

## 50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

实现pow（x，n），计算x升至幂n（x**n）

**Example:1**

```
Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

---

### Python Solution
**分析：** 简单快速幂的求法。

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        p, r = abs(n), 1
        while p:
            if p & 1:
                r *= x
            x *= x
            p >>= 1
        return r if n >= 0 else 1/r
```

[返回目录](#00)

## 204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

计算小于非负数n的质数数。

**Example:1**

```
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```

---

### Python Solution
**分析：** 最优化的素数生成。固定好空间，关键点在 sqrt(n) + 1 和 pr[i * i: n: i] = [0] * len(pr[i * i: n: i])

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        pr = [1] * n
        pr[0] = pr[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if pr[i]:
                pr[i * i: n: i] = [0] * len(pr[i * i: n: i])
        return sum(pr)
```

[返回目录](#00)

## 167. Two Sum II

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

给定已按升序排序的整数数组，找到两个数字，使它们相加到特定的目标数。
函数twoSum应返回两个数字的索引，以便它们加起来到目标，其中index1必须小于index2。

**Example**

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

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

## 611. Valid Triangle Number

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

给定一个由非负整数组成的数组，你的任务是计算从可以组成三角形的数组中选择的三元组的数量，如果我们将它们作为三角形的边长。

**Example**

```
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
```

---

### Python Solution
**分析：** 这道题是中等难度的题，但其实是 Two Sum 类型题的变形。非常漂亮的解法，如果暴力法的话需要 O(n^3) 的时间复杂度，但是如果巧妙运用双指针，可以缩减为 O(n^2) 。我们按照从短到长将边设为 a, b, c 三边，排序后从最后取 c 的值，如果边 a 和边 b 的长度超过边 c 的长度，那么直接加上可能的个数 (b - a)，否则移动 a 使得相加之和变大。

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for c in range(len(nums) - 1, 1, -1):
            a, b = 0, c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    res += b - a
                    b -= 1
                else:
                    a += 1
        return res
```

[返回目录](#00)

## 202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

编写算法以确定数字是否为“ happy”。 一个快乐的数字是由以下过程定义的数字：以任何正整数开头，用该数字的平方和代替该数字，然后重复该过程，直到该数字等于1（它将停留在该位置），否则它就会循环 在不包含1的循环中无休止地循环。以1结尾的那些数字是快乐数字。

**Example**

```
Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

---

### Python Solution
**分析：** 用集合保留出现过的数字保证它不是在循环。

```python
class Solution:
    def isHappy(self, n):
        stop = {1}
        while n not in stop:
            stop.add(n)
            n = sum(int(d)**2 for d in str(n))
        return n == 1
```

[返回目录](#00)

## 263. Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

编写程序以检查给定的数字是否是丑陋的数字。 丑数是正数，其主要因子仅包括2、3、5。

**Example**

```
Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
```

---

### Python Solution
**分析：** 只是简单地判断一个数是不是丑数。num % p == 0 用来确保这个数能被当前因子整除，num > 1 用来最后跳出循环。

```python
class Solution:
    def isUgly(self, num: int) -> bool:
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1
```

[返回目录](#00)

## 264. Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

编写程序以查找第n个丑数。 丑数是正数，其主要因子仅包括2、3、5。

**Example**

```
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
```

---

### Python Solution
**分析：** 第一种方案是一个一个生成丑数，计算到第 n 个即可，第二种方案是预运算之后进行排序，返回第 n 个。
面试中第二种会比较亮眼但是需要说明 32 20 14 的由来。

```python
class Solution:
    def nthUglyNumber(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]
```

```python
class Solution:
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n):
        return self.ugly[n-1]
```

[返回目录](#00)

## 343. Integer Break

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

给定一个正整数n，请将其分解为至少两个正整数的和，并使这些整数的乘积最大化。 返回您可以获得的最大产品。

**Example**

```
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

---

### Python Solution
**分析：** 动态规划做法和数学贪婪做法。

```python
class Solution(object):
    def integerBreak(self,n):
        dp = [0]*(n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], max(dp[j]*(i-j), j*(i-j)))
        return dp[n]
```

```python
class Solution(object):
    def integerBreak(self,n):
        return n - 1 if n < 4 else 3 ** ((n-2) // 3) * ((n-2) % 3 + 2)
```

[返回目录](#00)

## 357. Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10**n.

给定一个非负整数n，计算所有具有唯一数字x的数字，其中0≤x <10**n。

**Example**

```
Input: 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
             excluding 11,22,33,44,55,66,77,88,99
```

---

### Python Solution
**分析：** 简单数学概率题。

```python
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n < 1:
            return 1
        if n > 10:
            return 0
        ret = cur = d = 9
        for _ in range(n - 1):
            cur *= d
            ret += cur
            d -= 1
        return ret + 1
```

[返回目录](#00)

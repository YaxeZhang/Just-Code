<span id = "00"></span>
## 一维		
 - [70. Climbing Stairs](#70-climbing-stairs)
 - [53. Maximum Subarray](#53-maximum-subarray)
 - [62. Unique Paths](#62-unique-paths)
 - [63. Unique Paths II](#63-unique-paths-ii)
 - [120. Triangle	很少考](#120-triangle)
 - [279	Perfect Squares]
 - [139	Word Break]
 - [375	Guess Number Higher or Lower II]
 - [312	Burst Balloons]
 - [322	Coin Change]
## 股票最大利润问题
 - [121. Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock)
 - [122	Best Time to Buy and Sell Stock II]
 - [123	Best Time to Buy and Sell Stock III]
 - [188	Best Time to Buy and Sell Stock IV]
 - [309	Best Time to Buy and Sell Stock with Cooldown]
## 二维		
 - [256	Paint House]
 - [265	Paint House II]
 - [64	Minimum Path Sum]
 - [72	Edit Distance]
 - [97	Interleaving String]
 - [174	Dungeon Game]
 - [221	Maximal Square]
 - [85	Maximal Rectangle]
 - [363	Max Sum of Rectangle No Larger Than K]
## 化简		
 - [198	House Robber]
 - [213	House Robber II]
 - [276	Paint Fence]
 - [91	Decode Ways]
 - [10	Regular Expression Matching]
 - [44	Wildcard Matching]

## 70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

你正在爬楼梯。它需要n步才能达到顶峰。

每次你可以爬1或2步。您可以通过多少不同的方式登顶？

注意：给定n将是一个正整数。

**Example**

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

---

### Python Solution
**分析：** 从简单到难理解动态规划，即利用前面的子问题的解求得后面问题的解。不递归调用，而只是存储子问题解并且通过状态转移来解决。

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2,n):
            dp[i] = dp[i - 1] + dp[i- 2]
        return dp[-1]
```

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 0
        for _ in range(n + 1):
            a, b = a + b, a
        return b
```

[返回目录](#00)

## 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

给定一个整数数组nums，找到具有最大总和的连续子数组（至少包含一个数字）并返回其总和。

**Example**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

---

### Python Solution
**分析：** 动态规划做法及其优化。实际上用 best 存储当前 dp 的最大值， curr 存储 dp[i]。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
```

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)
        return best
```

[返回目录](#00)

## 62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

机器人位于 m x n 矩阵的左上角（在下图中标记为“开始”）。 机器人只能在任何时间点上下移动。 机器人试图到达网格的右下角（在下图中标记为“完成”）。 有多少种可能的独特路径？

**Example**

```
Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28
```

---

### Python Solution
**分析：**

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
```

**可简化为一维**

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]
```

**数学方法**

```python
from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(n+m-2) / (factorial(n-1) * factorial(m-1)))
```

[返回目录](#00)

## 63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

机器人位于m x n网格的左上角（在下图中标记为“开始”）。 机器人只能在任何时间点上下移动。 机器人试图到达网格的右下角（在下图中标记为“完成”）。 现在考虑是否在网格中添加了一些障碍。 会有多少条独特的路径？ 障碍物和空白区域在网格中分别标记为1和0。

**Example**

```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

---

### Python Solution
**分析：**

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for x in range(n)] for y in range(m)]
        #dp = [[0] * n] * m    和上一行的区别为这一行实际上是浅拷贝。非常不安全。
        i = j = 0
        while i < m and obstacleGrid[i][0] == 0:
                dp[i][0] = 1
                i += 1
        while j < n and obstacleGrid[0][j] == 0:
                dp[0][j] = 1
                j += 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
```

**可简化为一维**

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[j] = dp[j] + dp[j - 1]
                else:
                    dp[j] = 0
        return dp[-1]
```

[返回目录](#00)

## 120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

给定一个三角形，找到从上到下的最小路径总和。您可以将每一步移至下面一行中的相邻数字。

**Example**

```
For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
```

---

### Python Solution
**分析：** 从低向上找到更小的值合并到最开始的一个元素。

```python
class Solution(object):
    def minimumTotal(self, triangle):
        dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
```

**写成一行的形式：**

```python
class Solution(object):
    def minimumTotal(self, triangle):
        return reduce(lambda a, b:[min(a[i], a[i+1])+n for i, n in enumerate(b)], triangle[::-1])[0]
```

[返回目录](#00)

## 121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

假设您有一个数组，第i个元素是第i天给定股票的价格。

如果只允许您最多完成一笔交易（即买入和卖出一股股票），请设计一种算法以找到最大的利润。

**Example**

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

---

### Python Solution
**分析：**

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = 1 << 33
        for price in prices:
            if price < low:
                low = price
            elif price - low > profit:
                profit = price - low
        return profit
```

```python
class Solution:
    def maxProfit(self, prices):
        min_p, max_v = 1 << 33, 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_v = max(max_v, prices[i] - min_p)
        return max_v
```

[返回目录](#00)

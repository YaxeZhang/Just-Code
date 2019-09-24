<span id = "00"></span>
## 一维		
 - [70. Climbing Stairs](#70-climbing-stairs)
 - [53. Maximum Subarray](#53-maximum-subarray)
 - [62	Unique Paths]
 - [63	Unique Paths II]
 - [120	Triangle	很少考]
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
        dp = [0]*len(nums)
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

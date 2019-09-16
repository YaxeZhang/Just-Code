<span id = "00"></span>
## 一维		
 - [70. Climbing Stairs](#70-climbing-stairs)
 - [62	Unique Paths]
 - [63	Unique Paths II]
 - [120	Triangle	很少考]
 - [279	Perfect Squares]
 - [139	Word Break]
 - [375	Guess Number Higher or Lower II]
 - [312	Burst Balloons]
 - [322	Coin Change]
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

> Input: 2
> Output: 2
> Explanation: There are two ways to climb to the top.
> 1. 1 step + 1 step
> 2. 2 steps

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

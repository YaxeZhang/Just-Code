<span id = "00"></span>
## 一维		
 - [70. Climbing Stairs](#70-climbing-stairs)
 - [53. Maximum Subarray](#53-maximum-subarray)
 - [62. Unique Paths](#62-unique-paths)
 - [63. Unique Paths II](#63-unique-paths-ii)
 - [120. Triangle	很少考](#120-triangle)
 - [279. Perfect Squares](#279-perfect-squares)
 - [139. Word Break](#139-word-break)
 - [375. Guess Number Higher or Lower II](#375-guess-number-higher-or-lower-ii)
 - [312. Burst Balloons](#312-burst-balloons)
 - [322	Coin Change]
## 股票最大利润问题
 - [121. Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock)
 - [122. Best Time to Buy and Sell Stock II](#122-best-time-to-buy-and-sell-stock-ii)
 - [123	Best Time to Buy and Sell Stock III]
 - [188	Best Time to Buy and Sell Stock IV]
 - [309	Best Time to Buy and Sell Stock with Cooldown]
## 二维		
 - [256	Paint House] **?**
 - [265	Paint House II] **?**
 - [64. Minimum Path Sum](#64-minimum-path-sum)
 - [72	Edit Distance]
 - [97	Interleaving String]
 - [174	Dungeon Game]
 - [221. Maximal Square](#221-maximal-square)
 - [85	Maximal Rectangle]
 - [363	Max Sum of Rectangle No Larger Than K]
## 化简		
 - [198. House Robber](#198-house-robber)
 - [213	House Robber II]
 - [276	Paint Fence]
 - [91. Decode Ways](#91-decode-ways)
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

## 279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

给定一个正整数n，求和为n的最小平方数（例如1、4、9、16，...）。

**Example**

```
Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

---

### Python Solution
**分析：**  DP 解法。

```python
class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:   # 下面这句话的意思是求出所以能加一个平方数（即一个操作）到目前位置的dp[?]。
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
```

[返回目录](#00)

## 139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

给定一个非空字符串s和包含非空单词列表的字典wordDict，请确定s是否可以分段为一个或多个字典单词的以空格分隔的序列。

注意：

字典中的同一单词在细分中可能会重复使用多次。 您可能会认为词典中没有重复的单词。

**Example**

```
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

---

### Python Solution
**分析：** 两种解法，一种是逐个遍历，True表示可以到达这个地方，一直推导到最后一个,之所以是 len(s)+1 是因为最后一位必须要取到。另一种是递归的做法。

```python
class Solution:
    def wordBreak(self, s, words):
        ok = [True]
        max_len = max(map(len,words+['']))
        words = set(words)
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(max(0, i-max_len),i)),
        return ok[-1]
```

```python
class Solution:    # 效率很高!
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = dict()
        def helper(s):
            if not s: return True
            elif s in dic:
              return dic[s]
            else:
              dic[s]=any(helper(s[len(w):]) for w in wordDict if s.startswith(w))
              return dic[s]
        return helper(s)
```

[返回目录](#00)

## 375. Guess Number Higher or Lower II

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

我们正在玩猜猜游戏。 游戏如下：我选择一个从1到n的数字。 您必须猜测我选了哪个号码。 每次您猜错了，我都会告诉您我选的数字是高还是低。 但是，当您猜一个特定的数字x时，如果您猜错了，您需要支付$ x。 当您猜到我选的号码时，您就赢得了比赛。

**Example**

```
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
```

---

### Python Solution
**分析：** 一种是自下向上的带备忘录的动态规划，一种是递归的做法。

```python
class Solution(object):
    def getMoneyAmount(self, n):
        need = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])
                                   for x in range(lo, hi))
        return need[1][n]
```

```python
class Solution(object):
    def getMoneyAmount(self, n):
        def play(l = 1, h = n, dp = {}):
            if l >= h: return 0
            if (l, h) not in dp:
                dp[(l, h)] = min(g + max(play(l, g - 1, dp), play(g + 1, h, dp)) for g in range((l + h) / 2, h))
            return dp[(l, h)]

        return play()
```

[返回目录](#00)

## 312. Burst Balloons

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

给定n个气球，索引从0到n-1。 每个气球上都涂有一个数字，该数字由数组num表示。 要求您爆破所有气球。 如果您爆破气球i，您将获得nums [left] * nums [i] * nums [right]个硬币。 这里的左和右是i的相邻索引。 爆破后，左右会相邻。 明智地爆破气球，找到可以收集的最大硬币数。

**Example**

```
Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

---

### Python Solution
**分析：** 这道题没搞懂，感觉和暴力一样，头大。

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j - 2, -1, -1):
                ans = 0
                for mid in range(i + 1, j):
                    tmp = nums[i] * nums[mid] * nums[j] + dp[i][mid] + dp[mid][j]       
                    if tmp > ans: ans = tmp
                dp[i][j] = ans
        return dp[0][n - 1]
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

## 122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

假设您有一个数组，第i个元素是第i天给定股票的价格。 设计算法以找到最大的利润。 您可以根据需要完成尽可能多的交易（即，买入一份并多次出售一股股票）。 注意：您可能无法同时进行多项交易（即必须先出售股票才能再次购买）。

**Example**

```
Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

---

### Python Solution
**分析：** 两种解法：1. 动态规划的解法。 2. 贪心的解法，因为不限制买卖次数，所以我们只要后一天比前一天价格高，我们就在答案里加上差值，可以看作我们前一天买了今天买了，如果明天的比今天还高也没有关系，今天再买入、明天卖掉的方案和昨天买明天卖的方案是等价的。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp, j = [0] * n, n-1
        for i in range(n-2, -1, -1):
            if prices[i] > prices[i+1]:
                j = i
            dp[i] = dp[i+1] if i == j else prices[j] - prices[i] + dp[j]
        return dp[0] if dp else 0
```

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

# 可以简化为：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(b-a,0)for a,b in zip(prices,prices[1:]))
```

[返回目录](#00)

## 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

给定一个m×n的网格，其中填充有非负数，请找到一条从左上到右下的路径，该路径将沿其路径的所有数字的总和最小化。

注意：您只能在任何时间点向下或向右移动。

**Example**

```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

---

### Python Solution
**分析：** 二维的动态规划，是比较简单的题目，有点类似于[剑指 offer #47 礼物最大价值](https://github.com/YaxeZhang/Just-Interview/blob/master/%E5%89%91%E6%8C%87offer%EF%BC%88%E7%AC%AC%E4%BA%8C%E7%89%88%EF%BC%89/%E5%89%91%E6%8C%87offer%EF%BC%88%E7%AC%AC%E4%BA%8C%E7%89%88%EF%BC%89.md#47%E7%A4%BC%E7%89%A9%E7%9A%84%E6%9C%80%E5%A4%A7%E4%BB%B7%E5%80%BC)，但是区别在于最大价值对于第一行的初始化不用特意初始化，而求最小的值的话第一行是必须向后逐个累加的，所以第一行初始化要用前缀和。当然二维的可以写成一维的，这里就只给出一维 dp 的写法。

**一维的解法**

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0][:]
        for i in range(1, n):
            dp[i] += dp[i-1]
        for i in range(1, m):
            for j in range(n):
                if j > 0:
                    dp[j] = grid[i][j] + min(dp[j], dp[j-1])
                else:
                    dp[j] = grid[i][j] + dp[j]
        return dp[-1]
```

[返回目录](#00)

## 221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

给定一个填充有0和1的2D二进制矩阵，找到仅包含1的最大正方形并返回其面积。

**Example**

```
Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```

---

### Python Solution
**分析：** 二维的动态规划，将 dp[i][j] 作为矩形的右下角则只用考虑 dp[i-1][j], dp[i][j-1], A[i-1][j-1] 的最小值即可，当然也可以简化成一维的动态规划。而是否需要额外的空间来建立 dp 矩阵就看具体想法和要求了。

```python
class Solution:
    def maximalSquare(self, A):
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = int(A[i][j])
                if A[i][j] and i and j:
                    A[i][j] = min(A[i-1][j], A[i-1][j-1], A[i][j-1]) + 1
        return len(A) and max(map(max, A)) ** 2
```

**一维的解法**

```python
class Solution:
    def maximalSquare(self, A):
        area = 0
        if A:
            p = [0] * len(A[0])
            for row in A:
                s = list(map(int, row))
                for j, c in enumerate(s[1:], 1):
                    if s[j]:
                        s[j] = min(p[j-1], p[j], s[j-1]) + 1
                area = max(area, max(s) ** 2)
                p = s
        return area
```

[返回目录](#00)

## 198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

您是计划在街道上抢房屋的专业强盗。 每栋房屋都藏有一定数量的钱，阻止您抢劫每座房屋的唯一限制是相邻房屋都已连接了安全系统，如果在同一晚闯入两栋相邻房屋，它将自动与警方联系。 给定一个表示每个房屋的金额的非负整数列表，请确定您今晚可以盗用的最大金额，而无需通知警察。

**Example**

```
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

---

### Python Solution
**分析：** 当前房间偷不偷取决于上上间加当前房间的价值和上一间的值哪个大。状态方程在下面。当然 如果看穿了以后就可以简化成第二种写法。处理 base case 更干净简单。

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp = nums[:]
        dp[1] = max(dp[0], dp[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
```

**看破实质后的解脱**

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1
        return prev1
```

[返回目录](#00)

## 91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

使用以下映射，将包含AZ字母的消息编码为数字：'A'-> 1'B'-> 2 ...'Z'-> 26给定一个仅包含数字的非空字符串，请确定解码方式的总数。

**Example**

```
Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

---

### Python Solution
**分析：** 先智商判断一下，把 0 的情况排掉，规避很多不好做的条件。

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        s = s.replace('20', '')
        s = s.replace('10', '')
        if '0' in s: return 0
        l = r = 1
        for i in range(len(s)-1):
            if s[i] == '1' or s[i] == '2' and s[i+1] < '7':
                l, r = r, l+r
            else:
                l = r
        return r
```

[返回目录](#00)

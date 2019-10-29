<span id = "00"></span>
## 基础
 - [278	First Bad Version]
 - [35	Search Insert Position]
 - [33	Search in Rotated Sorted Array]
 - [81	Search in Rotated Sorted Array II]
 - [153	Find Minimum in Rotated Sorted Array]
 - [154	Find Minimum in Rotated Sorted Array II]
 - [162	Find Peak Element]
 - [374. Guess Number Higher or Lower](#374-guess-number-higher-or-lower)
 - [34	Search for a Range]
 - [349	Intersection of Two Arrays]
 - [350	Intersection of Two Arrays II]
 - [315. Count of Smaller Numbers After Self](#315-count-of-smaller-numbers-after-self)
 - [300	Longest Increasing Subsequence]
 - [354	Russian Doll Envelopes]


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

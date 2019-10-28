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
 - [315	Count of Smaller Numbers After Self]
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

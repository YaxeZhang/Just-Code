<span id = "00"></span>
## 基础
 - [389	Find the Difference]
 - [136	Single Number]
 - [318	Maximum Product of Word Lengths]
## 很少考			
 - [393	UTF-8 Validation]
 - [201. Bitwise AND of Numbers Range](#201-bitwise-and-of-numbers-range)
 - [371	Sum of Two Integers emove Element]
 - [338	Counting Bits]
 - [89	Gray Code]
 - [268	Missing Number]
 - [191	Number of 1 Bits]
 - [190	Reverse Bits]
 - [137	Single Number II]
 - [260	Single Number III]


## 201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

给定范围[m，n]，其中0 <= m <= n <= 2147483647，返回此范围内所有数字的按位AND，包括端值。

**Example**

> Input: [5,7]
> Output: 4

---

### Python Solution
**分析：** 只要找到两端的公共部分即可。

```python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m and m != n:   # NOTE: break when m == 0
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift
```

[返回目录](#00)

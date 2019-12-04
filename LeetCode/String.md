<span id = "00"></span>
## 基础		
 - [28. Implement strStr()](#28-implement-strstr)
 - [14. Longest Common Prefix](14-longest-common-prefix)
 - [58	Length of Last Word]
 - [387	First Unique Character in a String]
 - [383. Ransom Note](#383-ransom-note)
 - [344	Reverse String]
 - [151	Reverse Words in a String]
 - [186	Reverse Words in a String II]
 - [345	Reverse Vowels of a String]
 - [205. Isomorphic Strings](#205-isomorphic-strings)
 - [293	Flip Game]
 - [294	Flip Game II]
 - [290. Word Pattern](#290-word-pattern)
 - [242. Valid Anagram](#242-valid-anagram)
 - [49. Group Anagrams](#49-group-anagrams)
 - [249	Group Shifted Strings]
 - [87	Scramble String]
 - [179. Largest Number](#179-largest-number)
 - [6. ZigZag Conversion](#6-zigzag-conversion)
 - [161	One Edit Distance]
 - [38	Count and Say]
 - [358	Rearrange String k Distance Apart]
 - [316	Remove Duplicate Letters]
 - [271	Encode and Decode Strings]
 - [168. Excel Sheet Column Title](#168-excel-sheet-column-title)
 - [171. Excel Sheet Column Number](#171-excel-sheet-column-number)
 - [13. Roman to Integer](#13-roman-to-integer)
 - [12. Integer to Roman](#12-integer-to-roman)
 - [273	Integer to English Words]
 - [246	Strobogrammatic Number]
 - [247	Strobogrammatic Number II]
 - [248	Strobogrammatic Number III]
## 提高		
 - [68	Text Justification]
 - [65. Valid Number](#65-valid-number)
 - [157	Read N Characters Given Read4]
 - [158	Read N Characters Given Read4 II - Call multiple times]
## Substring		
 - [76. Minimum Window Substring](#76-minimum-window-substring)
 - [30	Substring with Concatenation of All Words]()
 - [3. Longest Substring Without Repeating Characters](#3-longest-substring-without-repeating-characters)
 - [340	Longest Substring with At Most K Distinct Characters]
 - [395. Longest Substring with At Least K Repeating Characters](#395-longest-substring-with-at-least-k-repeating-characters)
 - [159	Longest Substring with At Most Two Distinct Characters]
## Palindrome		
 - [125. Valid Palindrome](#125-valid-palindrome)
 - [266	Palindrome Permutation]
 - [5	Longest Palindromic Substring]
 - [9	Palindrome Number]
 - [214	Shortest Palindrome]
 - [336	Palindrome Pairs]
 - [131	Palindrome Partitioning]
 - [132	Palindrome Partitioning II]
 - [267	Palindrome Permutation II]
## Parentheses		
 - [20. Valid Parentheses](#20-valid-parentheses)
 - [22. Generate Parentheses](#22-generate-parentheses)
 - [32. Longest Valid Parentheses](#32-longest-valid-parentheses)
 - [241	Different Ways to Add Parentheses]
 - [301	Remove Invalid Parentheses]
## Subsequence		
 - [392. Is Subsequence](#392-is-subsequence)
 - [115	Distinct Subsequences]
 - [187	Repeated DNA Sequences]


## 28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

实现strStr（）。 返回大海捞针中第一次出现的针的索引，如果不属于大海捞针，则返回-1。

**Example**

```
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

---

### Python Solution
**分析：** 两种方法，一种是普通的方法但是已经优化，一种是马拉车算法。

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
```

```python
# TODO: 
```

[返回目录](#00)

## 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

编写一个函数以在字符串数组中找到最长的公共前缀字符串。 如果没有公共前缀，则返回一个空字符串“”。

**Example**

```
Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

---

### Python Solution
**分析：** 最长公共前缀 Python 里已经有实现了，但是面试考察点肯定不是这个，我们可以用 ASCII 码的排序来决定差的最大的两个字符串，方法一如下。当然我们可以用 zip(* ） 来转置 zip 的矩阵进行判断。解法如下：

```python
class Solution:
    def longestCommonPrefix(self, m):
        if not m: return ''
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
```

**Zip(* )**

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        sz, ret = zip(*strs), ""
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret
```

**Python 已经实现的 commonprefix**

```python
class Solution:
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)
```

[返回目录](#00)

## 383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

给定一个任意的赎金票据字符串和另一个包含所有杂志字母的字符串，编写一个函数，如果可以从杂志中构造赎金票据，则该函数将返回true； 否则，它将返回false。 杂志字符串中的每个字母只能在赎金记录中使用一次。

**Example**

```
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```

---

### Python Solution
**分析：** 一种是用 count，一种是用 Counter。

```python
class Solution:
   def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       for letter in set(ransomNote):
           if ransomNote.count(letter) > magazine.count(letter):
               return False
       return True
```

```python
class Solution:
    def canConstruct(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
```

[返回目录](#00)

## 205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

给定两个字符串s和t，确定它们是否同构。 如果可以替换s中的字符以获得t，则两个字符串是同构的。 在保留字符顺序的同时，必须将所有出现的字符替换为另一个字符。 没有两个字符可以映射到同一字符，但是一个字符可以映射到自身。

**Example**

```
Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
```

---

### Python Solution
**分析：** 简单题，主要考察 map 的映射关系。

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i, c in enumerate(s):
            if not c in d:
                if t[i] in d.values():
                    return False
                d[c] = t[i]
            else:
                if not d[c] == t[i]:
                    return False
        return True
```

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))
```

[返回目录](#00)

## 290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

给定一个模式和一个字符串str，找出str是否遵循相同的模式。 在此跟随是指完全匹配，因此模式中的字母与str中的非空单词之间存在双射

**Example**

```
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
```

---

### Python Solution
**分析：** 将单词字母转化为序列进行比较。

```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))
```

```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        f = lambda s: map({}.setdefault, s, range(len(s)))
        return list(f(pattern)) == list(f(str.split()))
```

[返回目录](#00)

## 242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

给定两个字符串s和t，编写一个函数来确定t是否是s的字谜。

**Example**

```
Input: s = "anagram", t = "nagaram"
Output: true
```

---

### Python Solution
**分析：** 简单题，用排序或者用字典。这里用的是内置的 Counter。

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

        return sorted(s) == sorted(t)
```

[返回目录](#00)

## 49. Group Anagrams

Given an array of strings, group anagrams together.

给定一个字符串数组，将字谜分组在一起。

**Example**

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

---

### Python Solution
**分析：** sorted 返回的是列表不能散列，所以用 tuple 封装一下。

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
```

[返回目录](#00)

## 179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

给定一个非负整数列表，将它们排列为最大的数字。

**Example**

```
Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
```

---

### Python Solution
**分析：** 有点冒泡排序的意思，比较 str(a)+str(b) < ? > str(b)+str(a) 那种大，来排序。

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums) == {0}: return "0"
        return "".join(sorted(map(str,nums),key = lambda x: x*3, reverse = True))

# 但这个 '3' 不科学，应该改为 len(str(max(nums))) - len(str(min(nums))) + 1
```

[返回目录](#00)

## 6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

字符串“ PAYPALISHIRING”以Z字形模式写在给定的行数上。

**Example**

```
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

---

### Python Solution
**分析：** 用 step 来决定前进方向。

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        zigzag = ["" for i in range(numRows)]
        row, step = 0, 1
        for char in s:
            zigzag[row] += char
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return "".join(zigzag)
```

[返回目录](#00)

## 168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

给定一个正整数，返回其相应的列标题，如Excel工作表中所示。

**Example**

```
1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB
...
```

---

### Python Solution
**分析：** 这是一道很简单的题，注意 (n - 1) % 26 而不是 n % 26 来避免 52 是 AZ 的情况。

```python
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n:
            n, mod = divmod(n - 1, 26)
            res = chr(mod + 65) + res
        return res
```

[返回目录](#00)

## 171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

给定列标题（如Excel工作表中所示），返回其对应的列号。

**Example**

```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
```

---

### Python Solution
**分析：** 这是一道很简单的题，不过可以用来熟悉 reduce 的用法。r 为之前叠加的结果，c 为当前的字符， s 是 c 取值的地方，0 是 r 的初始值。多用就熟悉了。

```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in s:
            res = res * 26 + ord(i) - 64
        return res
```

```python
from functools import reduce
class Solution:
    def titleToNumber(self, s: str) -> int:
        return reduce(lambda r, c: 26*r + ord(c)-64, s, 0)
```

[返回目录](#00)

## 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

罗马数字由七个不同的符号表示：I，V，X，L，C，D和M.符号值I 1 V 5 X 10 L 50 C 100 D 500 M 1000例如，两个以罗马数字II表示，只是两个加在一起。十二写为XII，简称X + II。数字二十七写为XXVII，即XX + V + II。罗马数字通常从左到右从大到小书写。但是，四个数字不是IIII。取而代之的是，数字四被写为IV。因为一个在五之前，所以我们减去它等于四。相同的原则适用于编号为IX的数字9。在六种情况下使用减法：我可以放在V（5）和X（10）之前以得到4和9.X可以放在L（50）和C（100）之前以得到40和90。可以放在D（500）和M（1000）的前面，以得到400和900。给定罗马数字，请将其转换为整数。输入保证在1到3999的范围内。

**Example**

```
Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

---

### Python Solution
**分析：** 用字典会简单很多，再用 mini 存储当前较小值来判断加还是减。

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = mini = 0
        for i in s[::-1]:
            if dic[i] < mini:
                res -= dic[i]
            else:
                res += dic[i]
            mini = dic[i]
        return res
```

[返回目录](#00)

## 12. Integer to Roman

题目就是上一道题的反向程序

**Example**

```
Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

---

### Python Solution
**分析：** 没有什么意义的题目。

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
```

[返回目录](#00)

## 65. Valid Number

Validate if a given string can be interpreted as a decimal number.

验证给定的字符串是否可以解释为十进制数字。

**Example**

```
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
```

---

### Python Solution
**两种写法**： 第一种是一次遍历所有条件判断，第二种就好理解很多。

```python
class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif char == '.':
                if met_dot or met_e: return False
                met_dot = True
            elif char == 'e' or char == 'E':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit
```

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        validList = set(['+', '-', '.', 'e', 'E'])
        isFirst = True

        for c in s:
            if c.isdigit():
                isFirst = False
                continue
            if c not in validList:
                return False
            if c == 'e' or c == 'E':
                if isFirst:
                    return False
                isFirst = True
                validList = set(['+', '-'])
            if c == '.':
                validList = set(['e', 'E'])
            if c == '+' or c == '-':
                if not isFirst:
                    return False
                validList.remove('+')
                validList.remove('-')

        return True and not isFirst
```

[返回目录](#00)

## 76 Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

给定一个字符串S和一个字符串T，找到S中的最小窗口，它将包含复杂度为O（n）的T中的所有字符。

**Example**

```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

---

### Python Solution
**分析：** 这是一道 Hard 难度的题目，我们采用滑动窗口来解决。用 need 来储存我们现在还需要的元素及其个数（可以为负），missing 代表我们现在还需要的元素的个数。小写的 i， j 是当前窗口的索引，大写的 I， J 是返回的结果窗口的索引。

```python
class Solution:
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0              # 如果存在 need[c] ，missing 减一
            need[c] -= 1
            if not missing:                     # 匹配到了所有需要的元素
                while i < j and need[s[i]] < 0: # 我们找到了此时满足条件的 j
                    need[s[i]] += 1             # 现在将 i 往后移动得到满足条件的最靠近的 i
                    i += 1
                if not J or j - i <= J - I:     # 初始化结果窗口和满足条件时更新窗口
                    I, J = i, j
                missing += 1                    # 将此时满足条件的 s[i] 丢失
                need[s[i]] += 1                 # 来求下一次满足的窗口
                i += 1
        return s[I:J]
```

[返回目录](#00)

## 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

给定一个字符串，找到最长子字符串的长度而不重复字符。

**Example:1**

```
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example:2**

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example:3**

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

---

### Python Solution
**分析：** 滑动窗口解决问题，如果遍历一遍 s，如果遍历到没有出现的元素，窗口右端立马扩张，并计算最大长度。如果遍历到之前出现的元素，则将窗口左端置为上次出现的位置的后一位。只有出现没有遍历过的元素才会计算最大长度。因为一旦是遍历过的元素，只有可能是保持不变或者缩小。

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        used = {}
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            used[c] = i
        return maxLength
```

[返回目录](#00)

## 395. Longest Substring with At Least K Repeating Characters

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

找到给定字符串的最长子字符串T的长度（仅由小写字母组成），以使T中的每个字符出现不少于k次。

**Example:1**

```
Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
```

**Example:2**

```
Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
```

---

### Python Solution
**分析：** 递归归并解决问题。

```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max([self.longestSubstring(i, k) for i in s.split(c)])
        return len(s)
```

[返回目录](#00)

## 125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

给定一个字符串，确定它是否是回文，只考虑字母数字字符并忽略大小写。 注意：出于此问题的目的，我们将空字符串定义为有效的回文。

**Example**

```
Input: "A man, a plan, a canal: Panama"
Output: true
```

---

### Python Solution
**分析：** 很容易想到我们如果先用 isalnum() 将字符或者数字选出来是不是就转换成了判断字符串是不是回文字符串的问题。那么我们用 Python 的列表推导式就可以 Pythonic 地解决这个要求。

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalpha() or i.isdigit()]
        return s == s[::-1]
```

**进阶** 但实际上我们的构成新列表 s 的操作时间复杂度为 O(n)， 空间复杂度为 O(n)。之后的进行判断是否为回文字符串的操作话费相同，显得比较粗鲁。因此我们想能不能更优雅地解决判断回文字符串的要求。于是有了下面的代码：

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
```

**再进阶** 利用双指针一前一后进行判断是否相同只要 O(n) 时间复杂度和 O(1) 的空间复杂度，比之前更有效率了。但是列表 s 仍然会花费 O(n) 的空间，所以我们将双指针不再局限在筛选后的 list 上，而是在原来的字符串上就开始工作。一前一后逼近，每次移动后判断当前位是否为字符或者数字，然后进行比较。这样只对字符串进行了一次遍历，所以只用了 O(n) 的时间复杂度，而且空间复杂度为 O(1) 。

```python
class Solution:
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return 0
            i += 1
            j -= 1
        return True
```

[返回目录](#00)

## 20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

给定仅包含字符'（'，'）'，'{'，'}'，'['和']'的字符串，请确定输入字符串是否有效。 在以下情况下，输入字符串有效：•开括号必须用相同类型的括号闭合。 开括号必须以正确的顺序关闭。

**Example**

```
Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
```

---

### Python Solution
**分析：** 简单题，栈的简单应用

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in ')]}':
                if not stack: return False
                if stack[-1] != dic[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack

```

[返回目录](#00)

## 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

给定n对括号，编写一个函数以生成格式正确的括号的所有组合。

**Example**

```
For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

---

### Python Solution
**分析：** 第一种回溯法？， 第二种感觉有点暴力的意思，只不过智能一点

```python
class Solution(object):
    def generateParenthesis(self, N):
        def generate(p, left, right, pars = []):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                pars.append(p)
            return pars
        return generate('', N, N)
```

```python
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
```

[返回目录](#00)

## 32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

给定仅包含字符'（'和'）'的字符串，请找到最长的有效（格式正确）括号子字符串的长度。

**Example**

```
Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```

---

### Python Solution
**分析：** 算法是可以一步一步进步的，从暴力法到动态规划或者做括号题常用的栈，再到 O(1) 空间的做法。

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def check(s, sign):
            res = l = r = 0
            for i in s:
                if i == sign:
                    l += 1
                else:
                    r += 1
                if l == r:
                    res = max(res, 2 * r)
                elif r > l:
                    l = r = 0
            return res
        return max(check(s, '('), check(s[::-1], ')'))
```

[返回目录](#00)

## 392. Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

给定字符串s和字符串t，请检查s是否为t的子序列。 您可以假设s和t都只有小写英文字母。 t可能是一个很长的字符串（长度== 500,000），而s是一个短字符串（<= 100）。 字符串的子序列是一个新字符串，它是通过删除某些字符（可以是无字符）而不会干扰其余字符的相对位置而从原始字符串形成的。 （即，“ ace”是“ abcde”的子序列，而“ aec”则不是）。

**Example**

```
Example 1:
s = "abc", t = "ahbgdc"
Return true.

Example 2:
s = "axc", t = "ahbgdc"
Return false.
```

---

### Python Solution
**分析：** 这道题思路不难，难的是优化和拓展的思路。

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True
```

[返回目录](#00)

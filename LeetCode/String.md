<span id = "00"></span>
## 基础		
 - [28	Implement strStr()]
 - [14	Longest Common Prefix]
 - [58	Length of Last Word]
 - [387	First Unique Character in a String]
 - [383. Ransom Note](#383-ransom-note)
 - [344	Reverse String]
 - [151	Reverse Words in a String]
 - [186	Reverse Words in a String II]
 - [345	Reverse Vowels of a String]
 - [205	Isomorphic Strings]
 - [293	Flip Game]
 - [294	Flip Game II]
 - [290. Word Pattern](#290-word-pattern)
 - [242. Valid Anagram](#242-valid-anagram)
 - [49	Group Anagrams]
 - [249	Group Shifted Strings]
 - [87	Scramble String]
 - [179	Largest Number]
 - [6	ZigZag Conversion]
 - [161	One Edit Distance]
 - [38	Count and Say]
 - [358	Rearrange String k Distance Apart]
 - [316	Remove Duplicate Letters]
 - [271	Encode and Decode Strings]
 - [168	Excel Sheet Column Title]
 - [171	Excel Sheet Column Number]
 - [13	Roman to Integer]
 - [12	Integer to Roman]
 - [273	Integer to English Words]
 - [246	Strobogrammatic Number]
 - [247	Strobogrammatic Number II]
 - [248	Strobogrammatic Number III]
## 提高		
 - [68	Text Justification]
 - [65	Valid Number]
 - [157	Read N Characters Given Read4]
 - [158	Read N Characters Given Read4 II - Call multiple times]
## Substring		
 - [76. Minimum Window Substring](#76-minimum-window-substring)
 - [30	Substring with Concatenation of All Words]()
 - [3. Longest Substring Without Repeating Characters](#3-longest-substring-without-repeating-characters)
 - [340	Longest Substring with At Most K Distinct Characters]
 - [395	Longest Substring with At Least K Repeating Characters]
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
 - [20	Valid Parentheses]
 - [22	Generate Parentheses]
 - [32	Longest Valid Parentheses]
 - [241	Different Ways to Add Parentheses]
 - [301	Remove Invalid Parentheses]
## Subsequence		
 - [392	Is Subsequence]
 - [115	Distinct Subsequences]
 - [187	Repeated DNA Sequences]


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

## 3 Longest Substring Without Repeating Characters

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

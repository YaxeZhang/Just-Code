<span id = "00"></span>
## 基础		
 - [28	Implement strStr()]
 - [14	Longest Common Prefix]
 - [58	Length of Last Word]
 - [387	First Unique Character in a String]
 - [383	Ransom Note]
 - [344	Reverse String]
 - [151	Reverse Words in a String]
 - [186	Reverse Words in a String II]
 - [345	Reverse Vowels of a String]
 - [205	Isomorphic Strings]
 - [293	Flip Game]
 - [294	Flip Game II]
 - [290	Word Pattern]
 - [242	Valid Anagram]
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
 - [125	Valid Palindrome]
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


## 76 Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

给定一个字符串S和一个字符串T，找到S中的最小窗口，它将包含复杂度为O（n）的T中的所有字符。

**Example**

> Input: S = "ADOBECODEBANC", T = "ABC"
> Output: "BANC"

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

> Input: "abcabcbb"
> Output: 3
> Explanation: The answer is "abc", with the length of 3.

**Example:2**

> Input: "bbbbb"
> Output: 1
> Explanation: The answer is "b", with the length of 1.

**Example:3**

> Input: "pwwkew"
> Output: 3
> Explanation: The answer is "wke", with the length of 3.

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

 - [返回目录](#00)

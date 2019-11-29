class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = flag = 0
        count = collections.Counter(s)
        for i in count:
            if count[i] % 2 == 1 and not flag:
                flag = 1
            res += count[i] // 2
        return 2*res + flag
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = ""
        i = 0
        l = len(s)

        while i < l:
            end = i

            while end + 1 < l and s[end + 1] == s[i]:
                end += 1

            candidate = self.get_palindrome(s, i, end)

            if len(candidate) > len(longest):
                longest = candidate

            i = end + 1

        return longest

    #@staticmethod
    def get_palindrome(self, s, start, end):
        while start > 0 and end + 1 < len(s) and s[start - 1] == s[end +1]:
            start -= 1
            end += 1

        return s[start:end + 1]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = maxlength = 0
        for i, v in enumerate(s):
            if v in used and start <= used[v]:
                start = used[v] + 1
            else:
                maxlength = max(maxlength, i - start + 1)
            used[v] = i
        return maxlength
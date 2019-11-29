class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n+1)
        for i in range(m):
            cur = [0] * (n+1)
            for j in range(n):
                if text1[i] == text2[j]:
                    cur[j+1] = dp[j] + 1
                else:
                    cur[j+1] = max(cur[j], dp[j+1])
            dp = cur
        return dp[-1]
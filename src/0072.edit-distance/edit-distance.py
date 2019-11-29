class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n+1))
        for i in range(m):
            new = [i+1]
            for j in range(n):
                if word1[i] == word2[j]:
                    new.append(dp[j])
                else:
                    new.append(1 + min(dp[j], dp[j+1], new[-1]))
            dp = new
        return dp[-1]
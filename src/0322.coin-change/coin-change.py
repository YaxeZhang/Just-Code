class Solution:
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in range(1, amount + 1):
            dp[i] = 1 + min(dp[i - c] if i >= c else MAX for c in coins)
        return -1 if dp[-1] == MAX else dp[-1]
class Solution:
    def maxSumDivThree(self, nums):
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            dp = [max(dp[i], dp[(i - num) % 3] + num) for i in range(3)]
        return dp[0]
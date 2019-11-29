class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j - 2, -1, -1):
                ans = 0
                for mid in range(i + 1, j):
                    tmp = nums[i] * nums[mid] * nums[j] + dp[i][mid] + dp[mid][j]       
                    if tmp > ans: ans = tmp
                dp[i][j] = ans
        return dp[0][n - 1]
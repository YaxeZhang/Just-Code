class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * len(A)
        cur = 0
        for i in range(len(dp)):
            if i < K:
                cur = max(cur,A[i])
                dp[i] =cur*(i+1)
            else:
                cur = 0
                for k in range(1,K+1):
                    cur = max(cur,A[i-k+1])
                    dp[i] = max(dp[i],dp[i-k]+cur*k)
        return dp[n-1]
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        
        dp = [0 for i in range(n + 1)]
    
        dp[0], dp[1] = 1, 1
        
        for i in range(2, n + 1):
            for j in range(i//2):
                dp[i] += dp[j] * dp[i - 1 - j] * 2
                # print(dp[i])
            
            if i % 2 != 0:
                dp[i] += dp[i//2] * dp[i//2]
                
        return dp[-1]
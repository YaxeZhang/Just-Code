class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        dp = [nums[0]]
        for n in nums[1:]:
            if n > dp[-1]:
                dp.append(n)
            else:
                pos = self.binarysearch(dp, n)
                dp[pos] = n
        return len(dp)
    
    def binarysearch(self, dp, n):
        lo, hi = 0, len(dp) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if dp[mid] < n:
                lo = mid + 1
            else:
                hi = mid
        return lo
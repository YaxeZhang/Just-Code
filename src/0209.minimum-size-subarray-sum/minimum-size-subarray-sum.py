class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, sum, res = 0, 0, float('inf')
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= s:
                i, sum, res = i + 1, sum - nums[i], min(res, j - i + 1)
        return 0 if res == float('inf') else res
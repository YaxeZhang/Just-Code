class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)
        return best
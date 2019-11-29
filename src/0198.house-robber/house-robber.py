class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = cur = 0
        for i in range(len(nums)):
            cur, prev = max(prev + nums[i], cur), cur
        return cur
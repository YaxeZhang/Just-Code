class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rev = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            rev[i] *= rev[i-1] or 1
        return max(nums + rev)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums) - 1
        while i and nums[i] <= nums[i-1]:
            i -= 1
        if i > 0:
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = reversed(nums[i:])
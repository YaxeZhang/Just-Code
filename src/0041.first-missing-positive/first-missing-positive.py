class Solution:
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 0 <= nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
        return len(nums) + 1
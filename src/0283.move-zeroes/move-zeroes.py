class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i]:
                if i != k:
                    nums[i], nums[k] = nums[k], nums[i]
                k += 1
        
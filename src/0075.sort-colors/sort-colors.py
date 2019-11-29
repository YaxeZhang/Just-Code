class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = i = 0
        two = len(nums)
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j = 0, len(nums) - 1
        while i + 1 < j:
            mid = int(i + (j - i) / 2)
            if nums[mid] > nums[j]:
                i = mid
            else:
                j = mid
        if nums[i] > nums[j]:
            return nums[j]
        else:
            return nums[i]
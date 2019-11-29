class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:        
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                return mid
            else:
                left = mid
        return right
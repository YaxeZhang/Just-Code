class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        i,j = 0, len(nums) - 1
        while i + 1 < j:
            mid = int(i + (j - i) /  2)
            if nums[mid] > nums[j]:
                i = mid
            else:
                if nums[mid] < nums[j]:
                    j = mid
                else:
                    j -= 1
        if nums[i] <= nums[j]:
            return nums[i]
        else:
            return nums[j]
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
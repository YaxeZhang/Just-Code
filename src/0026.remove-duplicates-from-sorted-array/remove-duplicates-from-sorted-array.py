class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1
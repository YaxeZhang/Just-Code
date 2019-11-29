class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return None
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx
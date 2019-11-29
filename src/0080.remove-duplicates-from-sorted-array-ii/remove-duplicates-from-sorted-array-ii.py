class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return None
        idx, count = 0, 0
        for i in range(1, len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
                count = 0
            else:
                if count < 1:
                    idx += 1
                    nums[idx] = nums[i]
                    count += 1
        return idx + 1
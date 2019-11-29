class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for i in range(len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = nums[i]
                    count = 1
        return candidate
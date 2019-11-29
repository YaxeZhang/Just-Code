class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(nums) == len(set(nums)): return False
        for i in range(len(nums)):
            for j in range(1, k + 1):
                if i + j >= len(nums): break
                if abs(nums[i] - nums[i + j]) <= t: return True
        return False
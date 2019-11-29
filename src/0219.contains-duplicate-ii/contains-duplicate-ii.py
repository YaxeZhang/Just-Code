class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or k < 1:
            return False
        used = {}
        flag = False
        for i, v in enumerate(nums):
            if v in used and not flag:
                flag = (i - used[v] <= k)
            used[v] = i
        return flag
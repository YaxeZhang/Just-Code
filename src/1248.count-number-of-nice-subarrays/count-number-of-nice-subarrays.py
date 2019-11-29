class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = [i for i in range(len(nums)) if nums[i] % 2 == 1]
        if len(odd) < k: return 0
        res = 0
        odd = [-1] + odd + [len(nums)]
        for i in range(1, len(odd) - k):
            res += (odd[i]- odd[i-1]) * (odd[i + k] - odd[i + k - 1])
        return res
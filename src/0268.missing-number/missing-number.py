class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumn = int(n * (n + 1) / 2)
        return sumn - sum(nums)
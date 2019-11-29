class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for c in range(len(nums) - 1, 1, -1):
            a, b = 0, c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    res += b - a
                    b -= 1
                else:
                    a += 1
        return res
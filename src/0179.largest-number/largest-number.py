class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums) == {0}: return "0"
        return "".join(sorted(map(str,nums),key = lambda x: x*3, reverse = True))
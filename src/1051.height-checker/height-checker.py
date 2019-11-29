class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l = sorted(heights)
        c = sum([1 for i in range(len(l)) if l[i] != heights[i]])
        return c 
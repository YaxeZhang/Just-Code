class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
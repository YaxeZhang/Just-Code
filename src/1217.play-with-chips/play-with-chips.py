class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        tmp = sum([1 for i in chips if i % 2 == 0])
        return min(tmp, len(chips) - tmp)
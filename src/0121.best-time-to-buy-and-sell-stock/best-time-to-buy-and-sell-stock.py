class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p, max_v = float('inf'), 0
        for p in prices:
            min_p = min(min_p, p)
            max_v = max(max_v, p - min_p)
        return max_v
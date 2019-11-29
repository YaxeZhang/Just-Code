class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1 = hold2 = float('-inf')
        sold1 = sold2 = 0
        for v in prices:
            sold2 = max(sold2, hold2 + v)
            hold2 = max(hold2, sold1 - v)
            sold1 = max(sold1, hold1 + v)
            hold1 = max(hold1, -v)
        return  sold2
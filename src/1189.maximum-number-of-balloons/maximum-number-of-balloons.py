class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        x = collections.Counter(text)
        return min(x['b'], x['a'], x['l']//2, x['o']//2, x['n'])
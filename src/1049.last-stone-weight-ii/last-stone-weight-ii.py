class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        total = sum(stones)
        for stone in stones:
            dp |= {a+stone for a in dp}
        
        return min(abs(total - a - a) for a in dp)
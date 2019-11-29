class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            a = stones.pop()
            b = stones.pop()
            last = a - b
            if last:
                stones.append(last)
        return stones[0] if stones else 0
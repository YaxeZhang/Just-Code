class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(i) for i in J)
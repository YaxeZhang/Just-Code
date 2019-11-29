class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        while len(res) <= num:
            res += [x+1 for x in res]
        return res[:num+1]
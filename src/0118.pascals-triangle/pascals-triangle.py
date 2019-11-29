class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res += [[1] + [res[-1][i] + res[-1][i + 1] for i in range(len(res[-1]) - 1)] + [1]]
        return res
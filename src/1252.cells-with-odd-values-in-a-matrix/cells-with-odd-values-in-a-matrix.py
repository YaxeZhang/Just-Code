class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row, col = [False] * n, [False] * m
        for r, c in indices:
            row[r] ^= True
            col[c] ^= True
        return sum(ro ^ cl for ro in row for cl in col)
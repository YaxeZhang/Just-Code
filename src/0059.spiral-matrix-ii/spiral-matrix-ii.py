class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n: return []
        A, lo = [[n*n]], n*n
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [[ i for i in range(lo, hi)]] + [list(j) for j in zip(*A[::-1])]
        return A
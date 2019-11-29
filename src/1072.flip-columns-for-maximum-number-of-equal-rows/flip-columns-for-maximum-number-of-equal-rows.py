class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern = collections.defaultdict(int)
        for row in matrix:
            pattern[tuple(row)] += 1
            pattern[tuple(1 - c for c in row)] += 1
        
        return max(pattern.values())
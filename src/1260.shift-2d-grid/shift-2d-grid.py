class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        tmp = [i for x in grid for i in x]
        k %= len(tmp)
        tmp = tmp[-k:] + tmp[:-k]
        return [tmp[i:i+len(grid[0])] for i in range(0, len(tmp), len(grid[0]))]
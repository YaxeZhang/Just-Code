class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        r, c = row - 1, 0
        while r >= 0 and c < col:
            tmp = matrix[r][c]
            if tmp == target:
                return True
            elif tmp < target:
                c += 1
            else:
                r -= 1
        return False
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col0, rows, cols = 1, len(matrix), len(matrix[0])

        for i in range(0, rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(rows-1, -1, -1):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0

        print(matrix)
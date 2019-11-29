class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix) - 1
        column  = 0
        while row >= 0 and column <= len(matrix[0]) - 1:
            if matrix[row][column] < target:
                column += 1
            elif matrix[row][column] == target:
                return True
            else:
                row -= 1
        return False
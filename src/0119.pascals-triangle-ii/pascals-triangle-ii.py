class Solution:
    def getRow(self, rowIndex):
        res = [1] * (rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                res[j] += res[j-1]
        return res
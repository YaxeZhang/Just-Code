class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = mini = 0
        for i in s[::-1]:
            if dic[i] < mini:
                res -= dic[i] 
            else:
                res += dic[i]
            mini = dic[i]
        return res
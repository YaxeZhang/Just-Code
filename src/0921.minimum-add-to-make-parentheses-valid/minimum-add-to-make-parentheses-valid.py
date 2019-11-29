class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res = tmp = 0
        for i in S:
            if i == '(':
                tmp += 1
            elif i == ')' and tmp > 0:
                tmp -= 1
            else:
                res += 1
                tmp = 0
        return res + tmp
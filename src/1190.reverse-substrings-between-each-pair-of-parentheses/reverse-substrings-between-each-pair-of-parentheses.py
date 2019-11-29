class Solution:
    def reverseParentheses(self, s: str) -> str:
        res, tmp = [], []
        for i in s:
            if i == ')':
                while res[-1] != '(':
                    tmp.append(res.pop())
                res.pop()
                res += tmp
                tmp = []
            else:
                res.append(i)
        return ''.join(res)
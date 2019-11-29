class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        res = ''
        v = 0
        for i in range(len(S)):
            if S[i] == '(':
                count += 1
            elif S[i] == ')':
                count -= 1
                if count == 0:
                    res += S[v + 1 : i]
                    v = i + 1
        return res
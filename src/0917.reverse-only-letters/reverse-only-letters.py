class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        res = [False for i in range(len(S))]
        temp = []
        for i in range(len(S)):
            if S[i].isalpha():
                temp.insert(0,S[i])
            else:
                res[i] = S[i]
        for i in range(len(res)):
            if not res[i]:
                res[i] = temp.pop(0)
        return ''.join(res)
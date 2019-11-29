class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split()
        vowel = ['a','e','i','o','u']
        res = []
        for i in range(len(S)):
            if S[i][0].lower() in vowel:
                res.append(S[i] + 'ma' + 'a'*(i+1))
            else:
                res.append(S[i][1:]+S[i][0]+'ma' + 'a'*(i+1))
        return ' '.join(res)
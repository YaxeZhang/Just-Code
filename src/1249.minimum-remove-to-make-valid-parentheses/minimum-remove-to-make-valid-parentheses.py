class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        a = list(s)
        b = []
        for i, c in enumerate(a):
            if '(' == c:
                b += i,
            elif ')' == c:
                if b:
                    b.pop()
                else:
                    a[i] = ''
        while b:
            a[b.pop()] = ''
        return ''.join(a)
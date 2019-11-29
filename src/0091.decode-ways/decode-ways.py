class Solution:
    def numDecodings(self, s: str) -> int:
        s = s.replace('20', '')
        s = s.replace('10', '')
        if '0' in s: return 0
        l = r = 1
        for i in range(0, len(s)-1):
            if s[i] == '1' or s[i] == '2' and s[i+1] < '7':
                l, r = r, l+r
            else:
                l = r
        return r
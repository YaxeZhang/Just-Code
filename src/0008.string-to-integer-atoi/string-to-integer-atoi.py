class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in ('+', '-'):
            s = s[1:]
        ret = i = 0
        while i < len(s) and s[i].isdigit():
            ret = ret * 10 + ord(s[i]) - ord('0')
            i += 1
        return min(2**31-1, max(sign*ret, -2**31))
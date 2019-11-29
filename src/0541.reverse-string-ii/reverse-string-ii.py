class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for ind in range(0, len(s), 2*k):
            s = s[:ind] + s[ind:k+ind][::-1] + s[k+ind:]
            
        return s
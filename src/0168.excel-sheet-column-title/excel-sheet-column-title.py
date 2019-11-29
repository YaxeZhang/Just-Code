class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n:
            n, mod = divmod(n - 1, 26)
            res = chr(mod + 65) + res
        return res
    

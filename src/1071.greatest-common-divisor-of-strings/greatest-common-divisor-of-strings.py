import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a, b = len(str1), len(str2)
        c  = math.gcd(a, b)
        res = str2[:c]
        
        if res*(b//c) == str2 and res*(a//c)==str1:
            return res
        return ''
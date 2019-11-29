class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(eval('0b' + a) + eval('0b' + b))[2:]
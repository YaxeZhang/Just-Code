class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return N ^ ((1 << (len(bin(N)) - 2)) - 1)
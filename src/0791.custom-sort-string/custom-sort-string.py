class Solution:
    def customSortString(self, S: str, T: str) -> str:
        return ''.join(sorted(list(T), key=lambda x:S.find(x)))
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        len1, len2 = 0, 1
        while len1 != len2:
            len1 = len(s)
            for i in set(s):
                s = s.replace(i * k, '')
            len2 = len(s)
        return s
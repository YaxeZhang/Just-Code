class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split()])
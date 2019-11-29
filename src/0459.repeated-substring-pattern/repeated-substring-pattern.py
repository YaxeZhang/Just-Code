class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s[:]*2)[1:len(s)*2-1].find(s) != -1
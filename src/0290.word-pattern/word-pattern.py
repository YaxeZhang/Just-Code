class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        f = lambda s: map({}.setdefault, s, range(len(s)))
        return list(f(pattern)) == list(f(str.split()))
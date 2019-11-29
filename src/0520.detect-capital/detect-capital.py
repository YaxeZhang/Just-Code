class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.istitle() | word.isupper() | word.islower()
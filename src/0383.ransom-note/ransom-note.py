class Solution:
    def canConstruct(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
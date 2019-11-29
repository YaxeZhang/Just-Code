class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        for i, v in enumerate(s):
            if count[v] == 1:
                return i 
        return -1
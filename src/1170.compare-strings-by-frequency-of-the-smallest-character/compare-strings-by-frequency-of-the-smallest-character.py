from bisect import bisect_left

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:  
        queries = [-w.count(min(w)) for w in queries]
        words = sorted([-w.count(min(w)) for w in words])
        return [bisect_left(words, q) for q in queries]
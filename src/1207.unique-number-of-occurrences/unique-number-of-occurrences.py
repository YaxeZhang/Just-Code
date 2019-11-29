class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = collections.Counter(arr)
        return len(arr.values()) == len(set(arr.values()))
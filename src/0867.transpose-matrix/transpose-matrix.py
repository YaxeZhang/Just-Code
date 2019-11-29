class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return zip(*A)
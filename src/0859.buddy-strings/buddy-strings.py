class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if A == B:
            return len(set(A)) < len(A)
        else:
            res = [[i, j] for i, j in zip(A, B) if i != j]
            return len(res) == 2 and res[0] == res[1][::-1]
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            
            low = max(a1, b1)
            high = min(a2, b2)
            if low <= high:
                res += [low, high],
            if a2 < b2:
                i += 1
            else:
                j += 1
        return res
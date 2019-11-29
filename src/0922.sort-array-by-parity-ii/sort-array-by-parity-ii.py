class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        def get_odd():
            for i in range(1, len(A), 2):
                if not A[i] % 2:
                    yield i
        
        odd = get_odd()
        for i in range(0, len(A), 2):
            if A[i] % 2:
                j = next(odd)
                A[i], A[j] = A[j], A[i]
        
        return A
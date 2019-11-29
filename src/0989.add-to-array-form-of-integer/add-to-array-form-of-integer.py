class Solution:
    def addToArrayForm(self, A, K):
            for i in range(len(A))[::-1]:
                if not K: break
                A[i], K = (A[i] + K) % 10, (A[i] + K) // 10
            return [int(i) for i in str(K)] + A if K else A
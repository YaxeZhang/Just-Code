class Solution:
    def rotatedDigits(self, N: int) -> int:
        isValid = lambda X: any((D in '2569') for D in str(X)) and (not any((D in '347') for D in str(X)))
        return sum((1 if isValid(i) else 0) for i in range(1, N + 1))
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        pr = [1] * n
        pr[0] = pr[1] = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if pr[i]:
                pr[i * i: n: i] = [0] * len(pr[i * i: n: i])
        return sum(pr)
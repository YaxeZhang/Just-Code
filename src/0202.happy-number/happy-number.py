class Solution:
    def isHappy(self, n):
        stop = {1}
        while n not in stop:
            stop.add(n)
            n = sum(int(d)**2 for d in str(n))
        return n == 1
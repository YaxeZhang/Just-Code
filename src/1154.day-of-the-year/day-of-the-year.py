class Solution:
    def dayOfYear(self, d: str) -> int:
    	D, [y,m,d] = [31,28,31,30,31,30,31,31,30,31,30,31], [int(i) for i in d.split("-")]
    	return sum(D[:(m-1)]) + d + ((m > 2) and (((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0)))
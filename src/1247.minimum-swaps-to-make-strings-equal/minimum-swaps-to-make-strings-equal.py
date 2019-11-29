class Solution:
    def minimumSwap(self, s1, s2):
            x1 = 0
            y1 = 0
            for i in range(len(s1)):
                if s1[i] != s2[i] and s1[i] == "x":
                    x1 += 1
                if s1[i] != s2[i] and s1[i] == "y":
                    y1 += 1
            if (x1 + y1) % 2 != 0:
                return -1
            return x1 // 2 + y1 // 2 + 2 * (x1 % 2)
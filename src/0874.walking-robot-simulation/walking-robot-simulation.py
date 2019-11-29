class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        p, s, m = [0, 0, 90], set(tuple(o) for o in obstacles), 0
        for c in commands:
            if c == -1: p[2] = (p[2] - 90) % 360
            elif c == -2: p[2] = (p[2] + 90) % 360
            else:
                j, k = 1 if p[2] % 180 else 0, 1 if not p[2] or p[2] == 90 else -1
                for i in range(1, c+1):
                    p[j] += k
                    if (p[0], p[1]) in s: 
                        p[j] -= k
                        break
                m = max(m, p[0]**2 + p[1]**2)
        return m
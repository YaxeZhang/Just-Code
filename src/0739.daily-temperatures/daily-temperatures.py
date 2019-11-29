class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        next_large = [0]*len(T)
        sk = []
        
        for i in range(len(T)):
            while sk and T[sk[-1]] < T[i]:
                next_large[sk[-1]] = i - sk[-1]
                sk.pop()
            sk.append(i)
        return next_large
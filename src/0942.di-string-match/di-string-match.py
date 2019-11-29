class Solution:
    def diStringMatch(self, S):
        l, r, arr = 0, len(S), []
        for s in S:
            arr.append(l if s == "I" else r)
            l, r = l + (s == "I"), r - (s == "D")
        return arr + [l]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x : x[0])
        res = []
        l, r = intervals[0]
        for i in range(1, len(intervals)):
            il, ir = intervals[i]
            if r < il:
                res += [l, r],
                l, r = il, ir
            else:
                r = max(r, ir)
        res += [l, r],
        return res
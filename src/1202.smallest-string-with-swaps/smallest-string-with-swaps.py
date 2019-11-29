class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        pa = list(range(n))

        def find(i):
            while pa[i] != i:
                pa[i] = pa[pa[i]]
                i = pa[i]
            return i
        
        for u, v in pairs:
            pa[find(v)] = find(u)
        
        from collections import defaultdict
        ccs = defaultdict(list)
        
        for i in range(n):
            ccs[find(i)].append(i)
            
        ret = [''] * n
        for cc in ccs.values():
            chars = sorted([s[k] for k in cc])
            for i, c in zip(cc, chars):
                ret[i] = c

        return ''.join(ret)
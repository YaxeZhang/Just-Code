class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        while cpdomains:
            cnt, site = cpdomains.pop().split()
            for i in range(len(site)):
                if i == 0 or site[i-1] == '.':
                    if site[i:] in count:
                        count[site[i:]] += int(cnt)
                    else:
                        count[site[i:]] = int(cnt)
        return [str(count[x]) + ' ' + x for x in count]
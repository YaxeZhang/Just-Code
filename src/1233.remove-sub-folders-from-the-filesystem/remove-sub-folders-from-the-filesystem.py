class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder: return []
        folder.sort()
        ans, prev = [folder[0]], folder[0]+'/'
        for f in folder[1:]:
            if not f.startswith(prev):
                ans.append(f)
                prev = f+'/'
        return ans
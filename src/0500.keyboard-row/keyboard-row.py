class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rowA = 'qwertyuiopQWERTYUIOP'
        rowB = 'asdfghjklASDFGHJKL'
        rowC = 'zxcvbnmZXCVBNM'
        return [i for i in words if set(i).issubset(set(rowA)) or set(i).issubset(set(rowB)) or set(i).issubset(set(rowC))]

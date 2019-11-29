class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in ",;.?'!":
            paragraph = paragraph.replace(c, ' ')
        
        ls = paragraph.lower().split()
        
        dict ={}
        for char in ls:
            if char not in banned:
                if char not in dict:
                    
                    dict[char] = 1
                else:
                    
                    dict[char] += 1
        
        return max(dict,key=dict.get)
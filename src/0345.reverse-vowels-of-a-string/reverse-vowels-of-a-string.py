class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        left = 0
        right = len(s) - 1
        slist = list(s)
        
        while left < right:
            if slist[left] in vowels and slist[right] in vowels:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
            elif slist[left] in vowels:
                right -= 1
            elif slist[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
                
        return ''.join(slist)
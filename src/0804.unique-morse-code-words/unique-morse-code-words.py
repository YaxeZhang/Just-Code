import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        map_morse = dict(zip(list(string.ascii_lowercase),morse))
        result=set()
        
        for w in words:
            c=''
            for letter in w:
                c+=map_morse[letter]
            result.add(c)
        return len(result)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = { 
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'], 
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'], 
        }

        tmp = []
        if digits == '' :
            return 
        
        # recursion 
        def dfs(num, string, tmp):
            if num == len(digits):
                tmp.append(string)
                return
            for i in dict[digits[num]]:
                dfs(num+1, string+i, tmp)
        dfs(0, '', tmp)
        
        return tmp
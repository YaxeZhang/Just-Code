class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if i in '({[':
                res.append(i)
            else:
                if i == ']':
                    if not res or res[-1] != '[':
                        return False
                    else:
                        res.pop()
                elif i == '}':
                    if not res or res[-1] != '{':
                        return False
                    else:
                        res.pop()
                else:
                    if not res or res[-1] != '(':
                        return False
                    else:
                        res.pop()
        if not res:
            return True
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        pos = 0
        def parse():
            nonlocal pos
            c = expression[pos]
            pos += 1
            if c == 't':
                return True
            if c == 'f':
                return False
            if c == '!':
                pos += 1
                v = parse()
                pos += 1
                return not v

            isand = c == '&'
            v = isand
            pos += 1
            while True:
                x = parse()
                if isand:
                    v = v and x
                else:
                    v = v or x
                if expression[pos] == ')':
                    pos += 1
                    break
                pos += 1
            return v
        return parse()
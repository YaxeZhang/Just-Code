class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                i = int(i)
                stack.append(i)
            else:
                if i == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)
                elif i == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif i == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
        return stack[0]
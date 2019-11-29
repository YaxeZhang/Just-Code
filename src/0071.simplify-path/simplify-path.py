class Solution:
    def simplifyPath(self, path):
        stack = []
        for token in path.split('/'):
            if token in ('', '.'):
                pass
            elif token == '..':
                if stack: stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)
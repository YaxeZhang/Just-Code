### 简化路径
#### 题目
给定文件的绝对路径（Unix风格），请简化它。 或者换句话说，将其转换为规范路径。 在UNIX样式的文件系统中，为period。 指当前目录。 此外，双倍..会将目录上移。 有关更多信息，请参阅：Linux / Unix中的绝对路径与相对路径请注意，返回的规范路径必须始终以斜杠/开头，并且两个目录名称之间必须只有一个斜杠/。 最后的目录名称（如果存在的话）不得以/结尾。 同样，规范路径必须是代表绝对路径的最短字符串。
#### 解法
**分析：** 很简单，但是边界要考虑清楚，还有不合法输入，比如 "....." 。

```python
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
```

### 编码和解码TinyURL
#### 题目
TinyURL是URL缩短服务，您可以在其中输入URL，例如https://leetcode.com/problems/design-tinyurl，并返回短URL，例如http://tinyurl.com/4e9iAk。 设计TinyURL服务的编码和解码方法。 编码/解码算法的工作方式没有限制。 您只需要确保可以将URL编码为小URL，并且可以将小URL解码为原始URL。
#### 解法
**分析：** 62 ^ 6 次方就已经很够很够了，思路要解析一下。

```python
class Codec:

    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]
```

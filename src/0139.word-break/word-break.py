class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        
        def helper(s):
            if not s: return True
            elif s in dic: return dic[s]
            else:
                dic[s] = any(helper(s[len(w):]) for w in wordDict if s.startswith(w))
                return dic[s]
        
        return helper(s)
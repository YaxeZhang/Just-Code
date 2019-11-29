class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = tmp = 0
        for i in s:
            if i == 'R':
                tmp += 1
            if i == 'L':
                tmp -= 1
            if not tmp:
                cnt += 1
        return cnt
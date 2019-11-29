class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in nums:
            if i:
                cnt += 1
            else:
                if cnt:
                    res = max(res, cnt)
                    cnt = 0
        return max(res, cnt)
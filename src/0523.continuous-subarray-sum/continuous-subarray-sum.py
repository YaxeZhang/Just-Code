class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = dict()
        d[0] = -1
        sums = 0

        for i in range(len(nums)):
            sums+=nums[i]
            sums = sums%(k or 2**32)
            if sums in d:
                if i-d[sums]>1:
                    return True
            else:
                d[sums] = i

        return False
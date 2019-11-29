from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums = map(str,nums)
        count = Counter(nums)
        return [x for x in count if count[x] == 1]
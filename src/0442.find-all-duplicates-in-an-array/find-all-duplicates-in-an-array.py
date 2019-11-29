class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [item for item,cnt in collections.Counter(nums).items() if cnt == 2]
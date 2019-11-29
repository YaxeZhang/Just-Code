class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, v in enumerate(nums):
            another = target - v
            if another not in dict:
                dict[v] = [another, i]
            else:
                return [dict[another][1],i]
            
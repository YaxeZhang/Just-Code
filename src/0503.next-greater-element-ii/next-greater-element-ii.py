class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        tmp = nums + nums
        stack, res = [], [-1] * len(nums)
        for i in range(len(tmp)):
            while stack and stack[-1][0] < tmp[i]:
                _, idx = stack.pop()
                if idx < len(nums):
                    res[idx] = tmp[i]
            stack.append((tmp[i], i))
        return res
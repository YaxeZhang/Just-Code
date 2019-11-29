class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for i in nums2:
            while stack and stack[-1] < i:
                d[stack.pop()] = i
            stack.append(i)
        res = []
        for i in nums1:
            res.append(d.get(i, -1))
        return res
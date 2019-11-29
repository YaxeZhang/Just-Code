class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = map(collections.Counter,(nums1, nums2))
        return list((a & b).elements())
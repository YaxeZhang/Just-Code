class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr_set = set(arr)
        result = []
        dist = 0
        while not result:
            dist += 1
            result = [ele for ele in arr if ele + dist in arr_set]
        return [[ele, ele+dist] for ele in sorted(result)]
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        tmp = []
        
        def binsrh(tmp, target):
            if not tmp:
                tmp.append(target)
                return 0
            if target > tmp[-1]:
                tmp.append(target)
                return len(tmp) - 1
            if target < tmp[0]:
                tmp[0:0] = [target]
                return 0
            i, j = 0, len(tmp) - 1
            while i < j:
                mid = (i + j) // 2
                if tmp[mid] >= target:
                    j = mid
                else:
                    i = mid + 1

            tmp[i:i] = [target]
            return i

        return [binsrh(tmp, nums[i]) for i in range(len(nums)-1, -1, -1)][::-1]
        return tmp
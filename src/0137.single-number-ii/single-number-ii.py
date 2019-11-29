class Solution:
    def singleNumber(self, nums):
        sum = 0
        ans = 0
        for i in range(32):
            sum = 0
            for n in nums:
                if (n >> i) & 1:
                    sum += 1
            if sum % 3:
                ans |= 1 << i
        return ans if ans < 2**31 else ans - 2**32
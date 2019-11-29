class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        res = []
        for i, v in enumerate(nums):
            while dq and nums[dq[-1]] < v:
                dq.pop()
            dq += i,
            if dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                res += nums[dq[0]],
        return res
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[len(height) - 1]
        res = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max > right_max:
                res += right_max - height[right]
                right -= 1
            else:
                res += left_max - height[left]
                left += 1
        return res
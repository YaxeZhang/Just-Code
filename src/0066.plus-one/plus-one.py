class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        digits.insert(0, 1)
        return digits
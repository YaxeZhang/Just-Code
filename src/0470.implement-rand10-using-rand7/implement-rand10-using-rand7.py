# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        idx = 40
        while idx >= 40:
            idx = 7*(rand7()-1) + rand7()-1
        return idx % 10 + 1
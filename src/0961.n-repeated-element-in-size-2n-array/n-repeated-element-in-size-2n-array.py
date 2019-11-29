from collections import Counter
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(1,4):#把问题放小就是大概率4个中有重复的，所以4个4个判断就可以了
            for k in range(len(A) - i):
                if A[k] == A[k + i]:
                    return A[k]
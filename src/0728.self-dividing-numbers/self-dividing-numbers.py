class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def f(d):
            for i in str(d):
                if i == '0' or d % int(i) > 0:
                    return False
            return True
        
        return [i for i in range(left, right + 1) if f(i)]
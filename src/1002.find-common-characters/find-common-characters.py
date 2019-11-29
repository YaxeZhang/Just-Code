class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        results = []
        i = 0
        while i <= len(A[0]) - 1:       # length of the first word will be decreasing so while is better than for
			# because while checks the condition after every loop
            if all(A[0][i] in item for item in A):      # check if char occures in every word
                results.append(A[0][i])         # if yes, add to results list
                A = [item.replace(A[0][i], '', 1) for item in A]        # return A list with words without first occurence of char
                i -= 1      # in case of deleting a char, deduct 1 to stay at the same index - 1 will be added in the next step
            i += 1

        return results
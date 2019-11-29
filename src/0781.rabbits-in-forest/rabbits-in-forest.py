from math import ceil

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
		# get the count of each rabbit's answer
        count_map = {}
        for ans in answers:
            if ans in count_map:
                count_map[ans] = count_map[ans] + 1
            else:
                count_map[ans] = int(1)
		# based on count, calculate min_rabbits
        result = 0        
        for (ans, count) in count_map.items():
            result += ceil(count / (ans+1)) * (ans+1)
            
        return result
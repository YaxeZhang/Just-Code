class Solution:
    def pathInZigZagTree(self, label):
        res = [] # O(log n) space
        node_count = 1
        level = 1
        # Determine level of the label
        while label >= node_count*2: # O(log n) time
            node_count *= 2
            level += 1
        # Iterate from the target label to the root
        while label != 0: # O(log n) time
            res.append(label)
            level_max = 2**(level) - 1
            level_min = 2**(level-1)
            label = int((level_max + level_min - label)/2)
            level -= 1
        return res[::-1] # O(log n) time
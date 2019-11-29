# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        level, res = [root], 0
        while level:
            res = level[0].val
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return res
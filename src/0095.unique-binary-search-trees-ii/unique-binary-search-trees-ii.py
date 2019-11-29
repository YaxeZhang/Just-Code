# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache
class Solution:
    def generateTrees(self, n):
        if not n: return []
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        @lru_cache(maxsize=None)
        def trees(first, last):
            return [node(root, left, right)
                    for root in range(first, last+1)
                    for left in trees(first, root-1)
                    for right in trees(root+1, last)] or [None]
        return trees(1, n)
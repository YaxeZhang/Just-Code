# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, node):
        if node:
            left, right = self.tree2str(node.left) or '', self.tree2str(node.right) or ''
            return f"{node.val}{f'({left})' if left or right else ''}{f'({right})' if right else ''}"
        return '' 
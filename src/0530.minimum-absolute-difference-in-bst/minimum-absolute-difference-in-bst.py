# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    pre = -float('inf')
    res = float('inf')

    def getMinimumDifference(self, root):
        if root.left:
            self.getMinimumDifference(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.getMinimumDifference(root.right)
        return self.res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        res = depth = 1
        Max = float('-inf')
        if root:
            level = [root]
            while level:
                tmp = sum([node.val for node in level])
                if tmp > Max:
                    Max = tmp
                    res = depth
                level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
                depth += 1
        return res
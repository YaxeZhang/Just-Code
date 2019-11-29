# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return -1 if len(res) < 2 else sorted(res)[1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, res = [(root, str(root.val))], 0
        while stack:
            node, st = stack.pop()
            if not node.left and not node.right:
                res += int(st)
            if node.left:
                stack.append((node.left, st + str(node.left.val)))
            if node.right:
                stack.append((node.right, st + str(node.right.val)))
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        stack, res = [(root, 0, None)], []
        while stack:
            node, dep, p = stack.pop()
            if node.val == x or node.val == y:
                res.append((dep, p))
            if node.left:
                stack.append((node.left, dep + 1, node))
            if node.right:
                stack.append((node.right, dep + 1, node))
        return res[0][0] == res[1][0] and res[0][1] != res[1][1]
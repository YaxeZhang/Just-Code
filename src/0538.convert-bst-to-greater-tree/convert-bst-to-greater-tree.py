# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        stack, res, tmp = [], 0, root
        while stack or root:
            while root:
                stack.append(root)
                root = root.right
            node = stack.pop()
            res += node.val
            node.val = res
            root = node.left
        return tmp
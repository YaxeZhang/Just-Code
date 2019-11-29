# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root, val):
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        pre = 0
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                p = stack.pop()
                if pre and p.val != pre:
                    return False
                pre = p.val
                root = p.right
        return True
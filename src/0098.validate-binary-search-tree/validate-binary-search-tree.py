# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        pre = None
        while len(stack) or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                p = stack.pop()
                if pre and p.val <= pre.val:
                    return False
                pre = p
                root = p.right
        return True
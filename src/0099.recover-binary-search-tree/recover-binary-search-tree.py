# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        pre = first = second = None
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val > root.val:
                second = root
                if not first:
                    first = pre
                else:
                    break
            pre = root
            root = root.right
        
        if first and second:
            first.val, second.val = second.val, first.val
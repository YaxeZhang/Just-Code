# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        if root:
            stack = [(root,False)]
            while stack:
                node, flag = stack.pop()
                if not node: continue
                if not node.left and not node.right:
                    if flag:
                        res += node.val
                else:
                    stack.append((node.left,True))
                    stack.append((node.right,False))
        return res
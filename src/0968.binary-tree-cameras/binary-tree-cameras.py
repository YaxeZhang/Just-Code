# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(root):
            if not root:
                return 2
            l = dfs(root.left)
            r = dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            if l == 1 or r == 1:
                return 2
            return 0
        
        return (dfs(root) == 0) + self.res
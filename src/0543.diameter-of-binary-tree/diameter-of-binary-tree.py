# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)
            return max(left, right) + 1
        
        dfs(root)
        return self.res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def dfs(root):
            if not root:
                return 0, 0
            left = dfs(root.left)
            right = dfs(root.right)
            return max(left) + max(right), root.val + left[0] + right[0]
        
        return max(dfs(root))
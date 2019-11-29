# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root):
            if root in (None, p, q):
                return root
            left, right = dfs(root.left), dfs(root.right)
            if left and right:
                return root
            if left:return left
            return right
        return dfs(root)
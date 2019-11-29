# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        
        def dfs(node):
            if node:
                dfs(node.right)
                node.val += self.sum
                self.sum = node.val
                dfs(node.left)
        
        dfs(root)
        return root
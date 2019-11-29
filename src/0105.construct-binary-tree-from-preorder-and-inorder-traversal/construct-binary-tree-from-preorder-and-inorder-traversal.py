# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(stop):
            if preorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = dfs(root.val)
                inorder.pop()
                root.right = dfs(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return dfs(None)
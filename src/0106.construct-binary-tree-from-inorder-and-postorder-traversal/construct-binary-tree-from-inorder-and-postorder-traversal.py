# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def postdfs(stop):
            if postorder and inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = postdfs(root.val)
                inorder.pop()
                root.left = postdfs(stop)
                return root
        return postdfs(None)
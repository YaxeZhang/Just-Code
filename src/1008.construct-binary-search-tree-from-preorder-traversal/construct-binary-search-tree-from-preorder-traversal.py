# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def predfs(stop):
            if preorder and preorder[-1] <= stop:
                root = TreeNode(preorder.pop())
                root.left = predfs(root.val)
                root.right = predfs(stop)
                return root
        preorder.reverse()
        return predfs(max(preorder))
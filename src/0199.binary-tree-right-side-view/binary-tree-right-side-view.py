# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            level = [root]
            while level:
                res.append(level[-1].val)
                level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return res
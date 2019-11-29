# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            level = [root]
            while level:
                res.append(max(x.val for x in level))
                level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return res
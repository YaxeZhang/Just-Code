# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root:
            level = [root]
            flag = 1
            while level:
                res.append([node.val for node in level][::flag])
                level = [kid for node in level for kid in (node.left, node.right) if kid]
                flag *= -1
        return res
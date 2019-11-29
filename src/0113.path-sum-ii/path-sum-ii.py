# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, tsum: int) -> List[List[int]]:
        if not root :
            return []
        temp, res = [], []
        def DFTS(root):
            temp.append(root.val)
            if not root.left and not root.right and sum(temp) == tsum:
                res.append(temp.copy())
            if root.left:
                DFTS(root.left)
            if root.right:
                DFTS(root.right)
            temp.pop()
        DFTS(root)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        level, res = [root], []
        while level:
            ll = [x.val for x in level]
            res.append(sum(ll) / len(ll))
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return res
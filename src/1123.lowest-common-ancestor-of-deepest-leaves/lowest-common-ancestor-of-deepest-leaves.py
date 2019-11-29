# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(root):
            if root is None:
                return [None,0]
            left = helper(root.left)
            right = helper(root.right)
            maxh = max(left[1],right[1])
            if left[1] < right[1]:
                return [right[0],maxh+1]
            elif left[1] > right[1]:
                return [left[0],maxh+1]
            else:
                return [root,maxh+1]
        res = helper(root)
        return res[0]
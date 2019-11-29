# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxLeft = self.maxHelper(root.left, root.val, root.val)
        maxRight = self.maxHelper(root.right, root.val, root.val)
        return max(maxLeft, maxRight)
    
    def maxHelper(self, root, minVal, maxVal):
        if not root:
            return abs(maxVal - minVal)
        
        if root.val < minVal:
            return max(self.maxHelper(root.left, root.val, maxVal), self.maxHelper(root.right, root.val, maxVal))
        elif root.val > maxVal:
            return max(self.maxHelper(root.left, minVal, root.val), self.maxHelper(root.right, minVal, root.val))
        else:
            return max(self.maxHelper(root.left, minVal, maxVal), self.maxHelper(root.right, minVal, maxVal))
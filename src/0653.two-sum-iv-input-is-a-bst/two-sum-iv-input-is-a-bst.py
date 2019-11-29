# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root, k):
            if not root: return False
            bfs, s = [root], set()
            for i in bfs:
                if k - i.val in s: return True
                s.add(i.val)
                if i.left: bfs.append(i.left)
                if i.right: bfs.append(i.right)
            return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: 
            return True
        q = collections.deque([(root.left, root.right)])
        while q:
            l, r = q.popleft()
            if l and r and l.val == r.val:
                q.extend([(l.right, r.left), (l.left, r.right)])
            elif l is r:
                continue
            else:
                return False
        return True
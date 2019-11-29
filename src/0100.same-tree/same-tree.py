# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        dq = collections.deque([(p, q)])
        while dq:
            n1, n2 = dq.popleft()
            if n1 and n2 and n1.val == n2.val:
                dq.extend([(n1.left, n2.left), (n1.right, n2.right)])
            elif n1 is n2:
                continue
            else:
                return False
        return True
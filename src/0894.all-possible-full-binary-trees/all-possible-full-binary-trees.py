# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    lookup = {1:[TreeNode(0)]}
    
    def allPossibleFBT(self, N):
        if N%2 == 0:
            return None
        if N not in Solution.lookup:
            ans = []
            for x in range(1,N,2):
                y = N - 1 -x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
            Solution.lookup[N] = ans
        return Solution.lookup[N]
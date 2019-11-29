# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        ans = 0
        
        while stack:
            node, sumval = stack.pop()
            if node.left or node.right:
                for kid in (node.left, node.right):
                    if kid:
                        stack.append((kid, kid.val + sumval*2))
            else:
                ans += sumval
                
        return ans
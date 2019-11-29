# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        q = [root]
        
        while q:
            node = q.pop(0)
            if node is None:
                return all(n is None for n in q)
            q.append(node.left)
            q.append(node.right)
            
        return True
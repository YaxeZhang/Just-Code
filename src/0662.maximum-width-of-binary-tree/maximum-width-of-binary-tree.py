# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        stack, res = [(root, 0, 0)], []
        while stack:
            node, depth, pos = stack.pop()
            if len(res) < depth + 1:
                res.append([])
            res[depth].append(pos)
            if node.left:
                stack.append((node.left, depth + 1, pos * 2))
            if node.right:
                stack.append((node.right, depth + 1, pos * 2 + 1))
        return max([max(res[i]) - min(res[i]) for i in range(len(res))]) + 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        result = collections.defaultdict(list)
        stack = [(root, 0)]
        while stack:
            new_stack = []
            cur_result = collections.defaultdict(list)
            for node, level in stack:
                cur_result[level].append(node.val)
                if node.left:
                    new_stack.append((node.left, level - 1))
                if node.right:
                    new_stack.append((node.right, level + 1))
            for i in cur_result:
                result[i].extend(sorted(cur_result[i]))
            stack = new_stack
        return [result[i] for i in sorted(result)]
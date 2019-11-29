"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root:
            level = [root]
            while level:
                res.append([x.val for x in level])
                level = [child for node in level for child in node.children if child]
        return res
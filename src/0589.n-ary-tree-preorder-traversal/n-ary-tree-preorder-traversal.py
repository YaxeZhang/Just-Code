"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        l = [root.val]
        for child in root.children:
            l.extend(self.preorder(child))
        return l
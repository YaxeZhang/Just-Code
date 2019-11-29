"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = [root.val]
        for child in root.children[::-1]:
            res.extend(self.postorder(child)[::-1])
        return res[::-1]
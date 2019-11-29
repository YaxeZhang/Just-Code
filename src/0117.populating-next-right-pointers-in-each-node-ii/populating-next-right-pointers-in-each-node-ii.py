"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        cur = [root]
        
        while cur:
            for i in range(len(cur) - 1):
                cur[i].next = cur[i+1]
            cur = [node for n in cur for node in (n.left, n.right) if node]
            
        return root
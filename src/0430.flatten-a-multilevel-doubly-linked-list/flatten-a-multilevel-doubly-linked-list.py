"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return  
        dummy = Node(0,None,head,None)
        
        stack = [head]
        prev = dummy
        
        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root
            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root        
          
        dummy.next.prev = None
        return dummy.next
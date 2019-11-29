"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p1 = p2 = p3 = head
        while p1:
            tmp = Node(p1.val, p1.next, None)
            p1.next = tmp
            p1 = p1.next.next
        while p2:
            tmp = p2.next
            tmp.random = p2.random.next if p2.random else None
            p2 = p2.next.next
        tmp = dummy = p3.next
        while p3:
            p3.next = tmp.next
            tmp.next = tmp.next.next if p3.next else None
            p3 = p3.next
            tmp = tmp.next
        return dummy
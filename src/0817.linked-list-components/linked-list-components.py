# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        cur = head
        res = 0
        while cur:
            if cur.val in G and getattr(cur.next, 'val', None) not in G:
                res += 1
            cur = cur.next
        return res
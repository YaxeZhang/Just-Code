# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre, node = None, slow
        while node:
            pre, pre.next, node = node, pre, node.next
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return
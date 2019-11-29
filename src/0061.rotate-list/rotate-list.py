# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        count = 1
        c = head
        while c.next:
            count += 1
            c = c.next
        c.next = head
        k %= count
        fast = head
        for _ in range(count - k - 1):
            fast = fast.next
        dummy = fast.next
        fast.next = None
        return dummy
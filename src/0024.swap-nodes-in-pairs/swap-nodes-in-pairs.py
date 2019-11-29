# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = tmp = ListNode(0)
        tmp.next = head
        while head and head.next:
            cur = head.next
            head.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            tmp, head = head, head.next
        return dummy.next
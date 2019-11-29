# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = less = ListNode(0)
        dummy2 = other = ListNode(0)
        while head:
            if head.val < x:
                less.next = less = head
            else:
                other.next = other = head
            head = head.next
        other.next = None
        less.next = dummy2.next
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = pre = ListNode(0)
        pre.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return dummy.next
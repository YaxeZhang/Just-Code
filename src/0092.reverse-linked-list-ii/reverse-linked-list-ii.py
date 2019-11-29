# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = post = ListNode(0)
        post.next = pre = head
        for _ in range(m-1):
            post, pre = pre, pre.next
        for _ in range(n-m):
            cur = pre.next
            pre.next = cur.next
            cur.next = post.next
            post.next = cur
        return dummy.next
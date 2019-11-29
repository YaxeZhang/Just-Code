# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pre = post =head
        while pre and pre.next:
            pre = pre.next.next
            post = post.next
        return post
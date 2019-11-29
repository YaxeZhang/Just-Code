# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        pre.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                pre.next = head.next
                head = head.next
            else:
                pre = pre.next
                head = head.next
        return dummy.next
    
    
    

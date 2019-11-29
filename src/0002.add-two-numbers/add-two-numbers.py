# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        dummy = p1 = ListNode(0); p2 = ListNode(0)
        p1.next , p2.next = l1, l2
        
        while p1.next and p2.next:
            p1, p2 = p1.next, p2.next
            sumval = p1.val + p2.val + flag
            p1.val = sumval % 10
            flag = sumval >= 10
            
        p1.next = p1.next or p2.next

        while flag and p1.next:
            p1 = p1.next
            if p1.val == 9:
                p1.val = 0
            else:
                p1.val += 1
                flag = 0
        
        if flag:
            while p1.next:
                p1 = p1.next
            p1.next = ListNode(1)
        
        return dummy.next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = tmp = ListNode(0)
        tmp.next = left = right = head
        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1
            if count == k:
                
                for _ in range(k-1):
                    cur = left.next
                    left.next = cur.next
                    cur.next = tmp.next
                    tmp.next = cur
                tmp, left = left, right
            else:
                return dummy.next
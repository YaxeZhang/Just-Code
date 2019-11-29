# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        hashMap, runningSum = {}, 0
        cur = head 
        while cur:
            runningSum += cur.val
            if runningSum == 0:
                head = cur.next
                hashMap.clear()
            else:
                if runningSum not in hashMap:
                    hashMap[runningSum] = cur 
                else:
                    pre = hashMap[runningSum]
                    sum2 = runningSum + pre.next.val
                    while sum2 != runningSum:
                        node = hashMap[sum2]
                        del hashMap[sum2]
                        sum2 += node.next.val
                    pre.next = cur.next                    
            cur = cur.next
        return head
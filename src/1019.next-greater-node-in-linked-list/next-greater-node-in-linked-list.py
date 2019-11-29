# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return None
        p, tmp, stack = head, [], []
        while p:
            tmp.append(p.val)
            p = p.next
        res = [0] * len(tmp)
        for i in range(len(tmp)):
            while stack and stack[-1][1] < tmp[i]:
                idx, _ = stack.pop()
                res[idx] = tmp[i]
            stack.append((i, tmp[i]))
            
        return res
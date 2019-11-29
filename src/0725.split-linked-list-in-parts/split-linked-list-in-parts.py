# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        length, cnt, res = 0, root, []
        while cnt:
            cnt = cnt.next
            length += 1
        div, mod = divmod(length, k)

        for _ in range(k):
            pre, post = root, None
            for _ in range(div + (mod != 0)):
                post, pre = pre, pre.next
            if post:
                post.next = None
            res.append(root)
            root = pre
            mod = mod - 1 if mod else 0
        return res
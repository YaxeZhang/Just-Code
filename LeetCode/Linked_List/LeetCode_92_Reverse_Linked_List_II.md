## 题目描述

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.


将位置m的链接列表反转到n。 只遍历一次。

注意：1≤m≤n≤列表长度。

**Example 1:**

> Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

---

## Python Solution
**分析：** 思路比较简单，可以参考[Reverse Linked List ](https://blog.csdn.net/Y_axe/article/details/99718252) 的解法，找到要反转的头和尾，进行反转操作即可

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = post = ListNode(0)
        pre = head
        post.next = head
        while m - 1:
            post = pre
            pre = pre.next
            m -= 1
            n -= 1
        while n - 1:
            pre = pre.next
            n -= 1
        ret = res = pre.next
        ans = post.next
        while ans != ret:
            tmp = ans.next
            ans.next = res
            res = ans
            ans = tmp
        post.next = res
        return dummy.next
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre, post = head, None
        for _ in range(m - 1):
            post = pre
            pre = pre.next
        for _ in range(n - m):
            cur = pre.next
            pre.next = cur.next
            if post:
                cur.next = post.next
                post.next = cur
            else:
                cur.next = head
                head = cur
        return head
```

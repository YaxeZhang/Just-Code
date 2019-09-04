## 题目描述

Reverse a singly linked list.

反转一个单链表

**Example 1:**

> Input: 1->2->3->4->5->NULL
> Output: 5->4->3->2->1->NULL

---

## Python Solution
**分析：** 反转链表是链表操作里比较经典的题型，操作为用一个单链表储存新的反转后的链表，原链表从前到后把每个节点和链表分开并且添加到新的单链表后边，再讲原链表的head指向head.next 完成head的后移。代码如下：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre
```

我们用的是Python，因为 Life is short, I use python.
**所以**!!!代码还可以简化成：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        while head:
            pre, pre.next, head = head, pre, head.next
        return pre
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        while head.next:
            cur = head.next
            head.next = cur.next
            cur.next = dummy.next
            dummy.next = cur
        return dummy.next
        
```

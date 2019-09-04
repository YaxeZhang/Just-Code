## 题目描述

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.


给定链表，交换每两个相邻结点并返回其头部。

您可能无法修改列表结点中的值，只能更改结点本身。

**Example 1:**

> Given 1->2->3->4, you should return the list as 2->1->4->3.

---

## Python Solution
**分析：** 我们如果要交换下两个结点，那么很容易想到：
1. 把当前结点的 next 指向下下个结点 
2. 把下下个结点的 next 指向当前结点的下个结点 
3. 把当前结点的下个结点的 next 指向下下下个结点
这样就完成了下两个结点的交换，把当前结点走到下下个结点即可。但是问题在于怎么区分 比如：当前结点是 tmp ，当前结点的下个结点是 tmp.next ，当前结点的下下个结点和当前结点的下个结点的 next 同样都是 tmp.next.next ，就产生了混淆歧义，于是分开他们就好了

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = tmp = ListNode(0)
        tmp.next = head
        while tmp.next and tmp.next.next:
            post = tmp.next
            pre = post.next
            tmp.next, pre.next, post.next = pre, post, pre.next
            tmp = post
        return dummy.next
```


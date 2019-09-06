## 题目描述
Given a linked list, remove the n-th node from the end of list and return its head.

给定一个链表，从列表末尾删除第n个节点并返回其头指针。

**Example :**

> Given linked list: **1->2->3->4->5**, and **n = 2**.
>
> After removing the second node from the end, the linked list becomes **1->2->3->5**.

**Note:**

Given n will always be valid.

---
## Python Solution
#### solution 1
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = post = dummy
        if not head:
            return None
        for i in range(n + 1):
            if not pre:
                return None
            pre = pre.next
        while pre:
            pre = pre.next
            post = post.next
        post.next = post.next.next
        return dummy.next
```
**分析：**
solution 1 是一次遍历中最常见的解法，dummy的存在避免了删除结点时删到了头结点的情况。我们要删除这个结点，那么要先找到这个结点的上一个结点并且讲上一个结点的next指给下一个结点。

在【剑指offer】中有一题是**找到**链表中倒数第 k 个结点，并返回。[链表中倒数第 k 个结点](https://blog.csdn.net/Y_axe/article/details/98678354) 我们这道题可以借鉴。如果利用这个我们可以这么写代码：

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = post = head
        for _ in range(n):   #没有判断是因为这里的 n 确定有效
            pre = pre.next
        if not pre:          #用来处理 pre 此时是头指针的情况
            return  head.next
        while pre.next:      #和剑指offer相比其实是提前了一位
            pre=pre.next
            post = post.next
        post.next = post.next.next
        return head
```

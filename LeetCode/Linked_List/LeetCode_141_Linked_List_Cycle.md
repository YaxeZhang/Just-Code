## 题目描述

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

给定一个链表，确定它是否有一个循环。

为了表示给定链表中的循环，我们使用整数pos来表示tail连接到的链表中的位置（0索引）。 如果pos为-1，则链表中没有循环。

**Example 1:**

> Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

**Example 2:**

> Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

**Example 3:**

> Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

---

## Python Solution
**分析：**

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
```

**Pythonic Solution:**

```Python
class Solution(object):
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
```

**更简洁！！**

```Python
class Solution(object):
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False
```

**破坏型解法，不推荐**

```Python
class Solution(object):
    def hasCycle(self, head):
        while head:
            if head.val == None:
                return True
            head.val = None
            head = head.next
        return False
```

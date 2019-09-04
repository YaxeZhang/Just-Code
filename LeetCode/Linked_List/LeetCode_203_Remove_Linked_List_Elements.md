## 题目描述
Remove all elements from a linked list of integers that have value val.

从链表中删除所有值等于 val 的结点

**Example**
```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

---

## Python Solution

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = pre = ListNode(0)
        pre.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return dummy.next
```

**分析：** 这道题在 LeetCode 中是 easy 的一道题。思维也很简单：复制一个一样的链表，然后逐个比较值，如果值相等则让上一个结点跳过这个结点指向下一个结点即可。空间复杂度为 O(n) ，，时间复杂度为 O(1) ，可以优化。
## 题目描述


Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

给定单链表，将所有奇数节点组合在一起，然后是偶数节点。 请注意，这里我们讨论的是节点编号，而不是节点中的值。

你应该尝试到位。 该程序应该以O（1）空间复杂度和O（节点）时间复杂度运行。

**Example 1:**

> Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

**Example 2:**

> Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

---

## Python Solution
**分析：** 将链表分成奇偶两条然后进行拼接即可，重点是边界判断

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd, even = head, head.next
        eventmp = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = eventmp
        return head
```

 

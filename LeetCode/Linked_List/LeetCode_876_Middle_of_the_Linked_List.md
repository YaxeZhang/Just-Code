## 题目描述
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

给定具有头节点头的非空的单链表，返回链表的中间节点。

如果有两个中间节点，则返回第二个中间节点。

**Example 1:**

> Input: [1,2,3,4,5] 
> Output: Node 3 from this list (Serialization:
> [3,4,5]) The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
>  Note that we returned a ListNode object ans,
> such that: 
> ans.val = 3, ans.next.val = 4,
>  ans.next.next.val = 5, and ans.next.next.next = NULL.

**Example 2:**

> Input: [1,2,3,4,5,6] 
> Output: Node 4 from this list (Serialization:[4,5,6]) 
> Since the list has two middle nodes with values 3 and 4, we
> return the second one.

---

## Python Solution
**分析：** 这道题在 LeetCode 中是 easy 的一道题。思维也很简单：1.先走一遍链表，**计算长度**。2.用math.ceil计算长度的一半取上值是多少。3.利用**快慢指针**进行计数找到要return的结点即可。

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        count =head
        while count:
            length += 1
            count = count.next
        length = math.ceil(length/2)
        
        pre = post =head
        for _ in range(length):
            pre = pre.next
        while pre:
            pre = pre.next
            post = post.next
        return post
```

##### 注意！
这里可能会有**疑问**：我们不是如果有两个中间结点的时候返回**后面的结点**么，那为什么用 math.ceil 向上取值，而不是用 math.floor 向下取值？
这里其实就是思路不清晰，如果有两个中间结点的时候肯定可以**整除**，而要用到 math 函数的时候其实是奇数个。

代码还可以简化成：

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pre = post =head
        while pre and pre.next:
            pre = pre.next.next
            post = post.next
        return post
```
快指针走两步，慢指针走一步来达到走到中间结点的目的。要注意判断条件，必须确定快指针的下一个、下下个结点都不为None。 

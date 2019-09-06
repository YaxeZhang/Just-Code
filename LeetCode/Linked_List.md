基础
[206  Reverse Linked List](#)
[141  Linked List Cycle](#)
[24	  Swap Nodes in Pairs](#)
[328  Odd Even Linked List](#)
[92   Reverse Linked List II](#)
[237  Delete Node in a Linked List](#)
[19   Remove Nth Node From End of List](#)
[83   Remove Duplicates from Sorted List](#)
[203  Remove Linked List Elements](#)
[82	  Remove Duplicates from Sorted List II](#)
[369  Plus One Linked List](#)
[2	  Add Two Numbers](#)
[160	Intersection of Two Linked Lists](#)
[21	  Merge Two Sorted Lists](#)
提高
[234	Palindrome Linked List](#)
[143	Reorder List](#)
[142	Linked List Cycle II](#)
[148  Sort List](#)
[25	  Reverse Nodes in k-Group](#)
[61	  Rotate List](#)
[86   Partition List](#)
[23   Merge k Sorted Lists](#)
[147	Insertion Sort List ](#)

## 206  Reverse Linked List

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

## 141  Linked List Cycle

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

## 24	  Swap Nodes in Pairs

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

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmp, tmp.next = self, head
        while tmp.next and tmp.next.next:
            post = tmp.next
            pre = post.next
            tmp.next, pre.next, post.next = pre, post, pre.next
            tmp = post
        return self.next
```

## 328  Odd Even Linked List

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

**Pythonic Solution:**

```python
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = head
        even = evenHead = odd.next
        while even and even.next:
            odd.next = odd = even.next
            even.next = even = odd.next
        odd.next = evenHead
        return head
```

## 92   Reverse Linked List II

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

## 237  Delete Node in a Linked List

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

编写一个函数来删除单链表中的节点（尾部除外），只允许访问该节点。

**Example 1:**

> Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

**Example 2:**

> Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

---

## Python Solution
**分析：** 有点蠢的题。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

## 19   Remove Nth Node From End of List

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

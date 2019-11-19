<span id = "00"></span>
## 基础
 - [206  Reverse Linked List](#206--reverse-linked-list)
 - [141  Linked List Cycle](#141--linked-list-cycle)
 - [876  Middle of the Linked List](#876--middle-of-the-linked-list)
 - [24	 Swap Nodes in Pairs](#24---swap-nodes-in-pairs)
 - [328  Odd Even Linked List](#328--odd-even-linked-list)
 - [92   Reverse Linked List II](#92---reverse-linked-list-ii)
 - [237  Delete Node in a Linked List](#237--delete-node-in-a-linked-list)
 - [19   Remove Nth Node From End of List](#19---remove-nth-node-from-end-of-list)
 - [83   Remove Duplicates from Sorted List](#83---remove-duplicates-from-sorted-list)
 - [203  Remove Linked List Elements](#203--remove-linked-list-elements)
 - [82   Remove Duplicates from Sorted List II](#82---remove-duplicates-from-sorted-list-ii)
 - [369  Plus One Linked List](#369--plus-one-linked-list)
 - [2	   Add Two Numbers](#2----add-two-numbers)
 - [445  Add Two Numbers II](#445--add-two-numbers-ii)
 - [160	 Intersection of Two Linked Lists](#160--intersection-of-two-linked-lists)
 - [21   Merge Two Sorted Lists](#21---merge-two-sorted-lists)
## 提高
 - [234	 Palindrome Linked List](#234--palindrome-linked-list)
 - [143	 Reorder List](#143--reorder-list)
 - [142  Linked List Cycle II](#142--linked-list-cycle-ii)
 - [430  Flatten a Multilevel Doubly Linked List](#430--flatten-a-multilevel-doubly-linked-list)
 - [114  Flatten Binary Tree to Linked List](#114--flatten-binary-tree-to-linked-list)
 - [148  Sort List](#148--sort-list)
 - [25   Reverse Nodes in k-Group](#25---reverse-nodes-in-k-group)
 - [61   Rotate List](#61---rotate-list)
 - [86   Partition List](#86---partition-list)
 - [23   Merge k Sorted Lists](#23---merge-k-sorted-lists)
 - [147	 Insertion Sort List](#147--insertion-sort-list)
 - [138  Copy List with Random Pointer](#138--copy-list-with-random-pointer)
 - [1019 Next Greater Node In Linked List](#1019-next-greater-node-in-linked-list)

## 206  Reverse Linked List

Reverse a singly linked list.

反转一个单链表

**Example 1:**

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

---

### Python Solution
**分析：** 反转链表是链表操作里比较经典的题型，操作为用一个单链表储存新的反转后的链表，原链表从前到后把每个节点和链表分开并且添加到新的单链表后边，再将原链表的head指向head.next 完成head的后移。代码如下：

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
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

[返回目录](#00)

## 141  Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

给定一个链表，确定它是否有一个循环。

为了表示给定链表中的循环，我们使用整数pos来表示tail连接到的链表中的位置（0索引）。 如果pos为-1，则链表中没有循环。

**Example 1:**

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

**Example 2:**

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

**Example 3:**

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

---

### Python Solution
**分析：**

```python
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow, fast = slow.next, fast.next.next
        return True
```

**Pythonic Solution:**

```Python
class Solution(object):
    def hasCycle(self, head):
        try:
            slow, fast = head, head.next
            while slow is not fast:
                slow, fast = slow.next, fast.next.next
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

[返回目录](#00)

## 876  Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

给定具有头节点头的非空的单链表，返回链表的中间节点。

如果有两个中间节点，则返回第二个中间节点。

**Example**

```
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
```

---

### Python Solution
**分析：**

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pre = post =head
        while pre and pre.next:
            post, pre = post.next, pre.next.next
        return post
```

[返回目录](#00)

## 24   Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.


给定链表，交换每两个相邻结点并返回其头部。

您可能无法修改列表结点中的值，只能更改结点本身。

**Example 1:**

```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

---

### Python Solution
**分析：** 我们如果要交换下两个结点，那么很容易想到：
1. 把当前结点的 next 指向下下个结点
2. 把下下个结点的 next 指向当前结点的下个结点
3. 把当前结点的下个结点的 next 指向下下下个结点
这样就完成了下两个结点的交换，把当前结点走到下下个结点即可。但是问题在于怎么区分 比如：当前结点是 tmp ，当前结点的下个结点是 tmp.next ，当前结点的下下个结点和当前结点的下个结点的 next 同样都是 tmp.next.next ，就产生了混淆歧义，于是分开他们就好了

```python
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

[返回目录](#00)

## 328  Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

给定单链表，将所有奇数节点组合在一起，然后是偶数节点。 请注意，这里我们讨论的是节点编号，而不是节点中的值。

你应该尝试到位。 该程序应该以O（1）空间复杂度和O（节点）时间复杂度运行。

**Example 1:**

```
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
```

**Example 2:**

```
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
```

---

### Python Solution
**分析：** 将链表分成奇偶两条然后进行拼接即可，重点是边界判断

```python
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

[返回目录](#00)

## 92   Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.


将位置m的链接列表反转到n。 只遍历一次。

注意：1≤m≤n≤列表长度。

**Example 1:**

```
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
```

---

### Python Solution
**分析：** 思路比较简单，可以参考[Reverse Linked List ](https://blog.csdn.net/Y_axe/article/details/99718252) 的解法，找到要反转的头和尾，进行反转操作即可

```python
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
        pre = head
        dummy = post = ListNode(0)
        post.next = head
        for i in range(m-1):
            post = pre
            pre = pre.next
        for i in range(n-m):
            cur = pre.next
            pre.next = cur.next
            cur.next = post.next
            post.next = cur
        return dummy.next
```

[返回目录](#00)

## 237  Delete Node in a Linked List

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

编写一个函数来删除单链表中的节点（尾部除外），只允许访问该节点。

**Example 1:**

```
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
```

**Example 2:**

```
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
```

---

### Python Solution
**分析：** 有点蠢的题。

```python
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

[返回目录](#00)

## 19   Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

给定一个链表，从列表末尾删除第n个节点并返回其头指针。

**Example :**

```
Given linked list: **1->2->3->4->5**, and **n = 2**.
After removing the second node from the end, the linked list becomes **1->2->3->5**.
```

**Note:**

Given n will always be valid.

---

#### Python Solution

#### solution 1
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = post = dummy
        if not head:
            return None
        for _ in range(n + 1):
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

在【剑指offer】中有一题是**找到**链表中倒数第 k 个结点，并返回。 - [链表中倒数第 k 个结点](https://blog.csdn.net/Y_axe/article/details/98678354) 我们这道题可以借鉴。如果利用这个我们可以这么写代码：

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = post = head
        for _ in range(n):   #没有判断是因为这里的 n 确定有效
            pre = pre.next
        if not pre:          #用来处理 pre 此时是头指针的情况
            return  head.next
        while pre.next:      #和剑指offer相比其实是提前了一位
            pre = pre.next
            post = post.next
        post.next = post.next.next
        return head
```

[返回目录](#00)

## 83   Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

给定已排序的链接列表，删除所有重复项，使每个元素只出现一次。

**Example 1:**

```
Input: 1->1->2
Output: 1->2
```

**Example 2:**

```
Input: 1->1->2->3->3
Output: 1->2->3
```

---

### Python Solution
**分析：**

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
```

[返回目录](#00)

## 203  Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

从具有值val的整数的链接列表中删除所有元素。

**Example 1:**

```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

---

### Python Solution
**分析：**

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

[返回目录](#00)

## 82   Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

给定已排序的链接列表，删除所有具有重复数字的节点，只留下原始列表中的不同数字。

**Example 1:**

```
Input: 1->2->3->3->4->4->5
Output: 1->2->5
```

**Example 2:**

```
Input: 1->1->1->2->3
Output: 2->3
```

---

### Python Solution
**分析：**

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        pre.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return dummy.next
```

[返回目录](#00)

## 369  Plus One Linked List

Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.

给定一个非负整数表示为非空的单个数字链表，整数加一。

存储数字使得最高有效数字位于列表的开头。

**Example**

```
Input: 1->2->3
Output: 1->2->4
```

---

### Python Solution
**分析：** 现将链表翻转然后找到第一位不为 9 的数字，加一再翻转回来，遍历过的为 9 的数字均置为 0 。

```python
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

# Two pointers solution.
class Solution(object):
    def plusOne(self, head):
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        left, right = dummy, head
        while right.next:
            if right.val != 9:
                left = right
            right = right.next
        if right.val != 9:
            right.val += 1
        else:
            left.val += 1
            right = left.next
            while right:
                right.val = 0
                right = right.next
        return dummy if dummy.val else dummy.next
```

[返回目录](#00)

## 2    Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

您将获得两个非空链表，表示两个非负整数。数字以相反的顺序存储，每个节点包含一个数字。添加两个数字并将其作为链接列表返回。

**Example**

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

---

### Python Solution
**分析：** 自我感觉十分优美的 O(1) 空间的解法，随便选一个链表作为主线，将相同长度的部分加上来，然后把剩余的部分拼接过来，如果有进位则顺理成章转化为 369，Plus One 问题。这里链表已经倒序，操作更加简便。

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        dummy = p1 = ListNode(0); p2 = ListNode(0)
        p1.next , p2.next = l1, l2

        while p1.next and p2.next:
            p1 = p1.next
            p2 = p2.next
            sumval = p1.val + p2.val + flag
            p1.val = sumval % 10
            flag = sumval >= 10

        p1.next = p1.next or p2.next

        while flag and p1.next:
            p1 = p1.next
            if p1.val == 9:
                p1.val = 0
            else:
                p1.val += 1
                flag = 0

        p1.next = ListNode(1) if flag else p1.next

        return dummy.next
```

[返回目录](#00)

## 445  Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

您将获得两个非空链表，它们代表两个非负整数。 最重要的数字在前，并且它们的每个节点都包含一个数字。 将两个数字相加，并将其作为链表返回。 您可能会假设两个数字除了数字0本身以外都不包含任何前导零。

跟进：如果无法修改输入列表怎么办？ 换句话说，不允许反转列表。

**Example**

```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```

---

### Python Solution
**分析：** 两种解法，一种和上题一样是原地操作的 O(1) 的空间，一种是创建新的链表。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def countlength(root):
            cnt = 0
            while root:
                root = root.next
                cnt += 1
            return cnt

        c1, c2 = l1, l2
        len1, len2 = countlength(c1), countlength(c2)
        if len2 > len1:
            len1, len2, l1, l2 = len2, len1, l2, l1
        dummy1 = tmp = tmp1 = ListNode(0)
        tmp.next = l1

        for _ in range(len1 - len2):
            tmp = tmp.next
            if tmp.val != 9:
                tmp1 = tmp

        cur = tmp.next
        while cur:
            val = cur.val + l2.val
            cur.val = val % 10
            if val < 9:
                tmp1 = cur
            elif val > 9:
                while tmp1 != cur:
                    tmp1.val = (tmp1.val + 1) % 10
                    tmp1 = tmp1.next
            cur, l2 = cur.next, l2.next

        return dummy1 if dummy1.val else dummy1.next
```

```python
class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if not l1 and not l2:
            return None

        l1_num = 0
        while l1:
            l1_num = l1_num * 10 + l1.val
            l1 = l1.next

        l2_num = 0
        while l2:
            l2_num = l2_num * 10 + l2.val
            l2 = l2.next

        lsum = l1_num + l2_num

        head = ListNode(None)
        cur = head
        for istr in str(lsum):
            cur.next = ListNode(int(istr))
            cur = cur.next

        return head.next
```

[返回目录](#00)

## 160  Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

编写程序以找到两个相交单链表的公共结点。

---

### Python Solution
**分析：** 两种解法，推荐第二种（显得高智商）。解法一：先遍历一次两个链表，获得它们的长度。因为有共同结点的话一定是共同结点之后都是相同的，所以让长的那个链表先走他们的长度之差，然后一同走直到两个链表的结点都是那一个。或者走到头，不存在公共结点。解法二：思路是将两个链表拼接，就可以忽略长度差，因为第二遍遍历时必定离末尾相同的距离。

```python
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lenA = lenB = 0
        h1, h2 = headA, headB

        while h1:
            h1 = h1.next
            lenA += 1

        while h2:
            h2 = h2.next
            lenB += 1

        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None
```

**Solution2:**

```python
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
```

[返回目录](#00)

## 21   Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

合并两个已排序的链接列表并将其作为新列表返回。 新列表应该通过拼接前两个列表的节点来完成。

**Example**

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

---

### Python Solution
**分析：** 进行比较哪个值小取哪个，然后被取值的往前走一步，没有比较之后把多的补到后面即可。

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tmp = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        tmp.next = l1 or l2
        return dummy.next
```

[返回目录](#00)

## 234  Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

给定一个单链表，确定它是否是回文。

**Example**

```
Input: 1->2->2->1
Output: true
```

---

### Pythonic Solution
**分析：** 快慢指针取到中间，同时翻转前半部与后半部比较。

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
```

[返回目录](#00)

## 143  Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

给定一个单链表L：L0→L1→…→Ln-1→Ln， 将其重新排序为：L0→Ln→L1→Ln-1→L2→Ln-2→…

您不能修改列表节点中的值，只能更改节点本身

**Example**

```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```

---

### Pythonic Solution
**分析：** 快慢指针取到中间，将后半部翻转然后两个链表交叉合并。

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        if not head:
            return

        # find the mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        pre, node = None, slow
        while node:
            pre, pre.next, node = node, pre, node.next

        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return
```

[返回目录](#00)

## 142  Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

给定一个链表，返回循环开始的节点。 如果没有循环，则返回null。

为了表示给定链表中的循环，我们使用一个整数pos表示尾部连接到的链表中的位置（索引为0）。 如果pos为-1，则链接列表中没有循环。

**Example1:**

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

**Example2:**

```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

---

### Pythonic Solution
**分析：** 快慢指针找到相交的那点后，一个从那个点出发另一个从头出发，相遇的点既是环的入口

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
```

[返回目录](#00)

## 430  Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

您将获得一个双向链接列表，该列表除了下一个和上一个指针外，还可以具有一个子指针，该子指针可以指向也可以不指向单独的双向链接列表。 这些子列表可能具有自己的一个或多个子列表，依此类推，以产生一个多级数据结构，如下例所示。 展平列表，以便所有节点都出现在单级双链接列表中。 您将获得列表第一级的头指针。

**Example1:**

```
Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
```

---

### Pythonic Solution
**分析：** 利用栈辅助来进行赋值。

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return  
        dummy = Node(0,None,head,None)

        stack = [head]
        prev = dummy

        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root
            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root        

        dummy.next.prev = None
        return dummy.next
```

[返回目录](#00)

## 114  Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

给定一棵二叉树，将其平整化为就地链表。

**Example1:**

```
For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

---

### Pythonic Solution
**分析：** 两种做法，一种是迭代实现，一种是递归实现。但都是利用一个值保存上一个或下一个结点。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:return
        stack = [root]
        tmp = None
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                node.left = None
                if tmp:
                    tmp.right = node
                tmp = node
```

```python
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
```

[返回目录](#00)

## 25   Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

给定一个链表，一次反转链表k的节点并返回其修改后的列表。

k是一个正整数，并且小于或等于链接列表的长度。 如果节点数不是k的倍数，那么最后剩下的节点应保持原样。

**Example**

```
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
```

---

### Pythonic Solution
**分析：** 利用 while True 和 count 进行循环计数，使得剩余满足 k 的时候才翻转，否则不变。如果 count 等于 k ，那么对于这一段的链表进行翻转即可。

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = tmp = ListNode(0)
        tmp.next = left = right = head
        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1
            if count == k:
                pre, cur = right, left
                for _ in range(k):
                    pre, pre.next, cur = cur, pre, cur.next
                tmp.next, tmp, left = pre, left, right
            else:
                return dummy.next
```

[返回目录](#00)

## 61   Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

给定一个链表，将列表向右旋转k个位置，其中k为非负数。

**Example1:**

```
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL.
```

**Example2:**

```
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
```

---

### Pythonic Solution
**分析：** k 大于链表长度时仍有效，所以先取得链表长度，k 对其取模，之后快慢指针找到倒数 k 的结点，从它的后一位将链表分为两部分，交换顺序即可。

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        c, count = head, 0
        while c:
            count += 1
            c = c.next
        k %= count
        if not k:
            return head
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next, dummy, slow.next = head, slow.next, None
        return dummy
```

[返回目录](#00)

## 86   Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

给定链表和值x，对其进行分区，使得小于x的所有节点都在大于或等于x的节点之前。

您应该保留两个分区中每个分区中节点的原始相对顺序。

**Example**

```
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
```

---

### Python Solution
**分析：**

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = less = ListNode(0)
        dummy2 = other = ListNode(0)
        while head:
            if head.val < x:
                less.next = less = head
            else:
                other.next = other = head
            head = head.next
        other.next = None
        less.next = dummy2.next
        return dummy.next
```

[返回目录](#00)

## 138  Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

给定一个链表，使每个节点包含一个附加的随机指针，该指针可以指向列表中的任何节点或为空。

返回列表的深层副本。

**Example**

```
Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
```

---

### Python Solution
**分析：**

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p1 = p2 = p3 = head

        while p1:
            tmp = Node(p1.val, p1.next, None)
            p1.next = tmp
            p1 = p1.next.next

        while p2:
            tmp = p2.next
            tmp.random = p2.random.next if p2.random else None
            p2 = p2.next.next

        tmp = dummy = p3.next
        while p3:
            p3.next = tmp.next
            tmp.next = tmp.next.next if p3.next else None
            p3 = p3.next
            tmp = tmp.next

        return dummy
```

[返回目录](#00)

## 1019 Next Greater Node In Linked List

We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

我们获得了一个链接列表，其中head为第一个节点。 让我们为列表中的节点编号：node_1，node_2，node_3等....

每个节点可能有一个更大的值：对于node_i，next_larger（node_i）是node_j.val，因此j> i，node_j.val> node_i.val，而j是最小的选择。 如果不存在这样的j，则下一个较大的值为0.

返回整数答案数组，其中answer [i] = next_larger（node_ {i + 1}）。

**Example**

```
Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
```

---

### Python Solution
**分析：** 1.Save the linked list values and access them from back to front for easy addition to list.
2.Use list to save the maximum value that occurred before.

```python
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return None
        p, tmp, stack = head, [], []
        while p:
            tmp.append(p.val)
            p = p.next
        res = [0] * len(tmp)
        for i in range(len(tmp)):
            while stack and stack[-1][1] < tmp[i]:
                idx, _ = stack.pop()
                res[idx] = tmp[i]
            stack.append((i, tmp[i]))

        return res
```

[返回目录](#00)

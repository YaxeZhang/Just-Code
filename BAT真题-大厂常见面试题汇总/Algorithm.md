

简化路径 #71
python 装饰器

洗牌算法
出现次数超过一半的数字
LC #862

区间合并问题

## 链表
 - [反转链表](#反转链表)<span id = "00"></span>
 - [两个一组反转链表](#两个一组反转链表)<span id = "01"></span>
 - [k个一组反转链表](#k个一组反转链表)<span id = "02"></span>
 - [奇偶次序分离后合并有序链表]
 - [两个链表求和]

## 二叉树
 - [二叉树的前序中序后序遍历]
 - [恢复二叉树（前序中序、后序中序）]
 - [二叉树翻转]
 - [二叉树的深度]
 - [平衡二叉树]
 - [二叉树的最大路径和]
 - [二叉树公共祖先]

## 动态规划
 - [unique path]
 - [换硬币]
 - [买卖股票的最佳时机]
 - [矩阵中的路径 jzoffer]
 - [正则表达式匹配 jzoffer]
 - [背包问题动态规划]
 - [子串之和的最大值]
 - [最长不重复子串]
 - [矩阵中最长递增子序列  LC #329]

## 二分查找
 - [数字在数组中的位置 jzoffer]
 - [排序数组进行二分查找，平移后的排序数组进行二分查找 #33]

## 排序算法
 - [冒泡排序]
 - [快速排序]
 - [归并排序]
 - [堆排序]
 - [桶排序]

## 双指针
 - [Two Sum]
 - [3 Sum]
 - [3 Sum Closest]
 - [搜索二维矩阵]

## 设计类
 - [min stack]
 - [LRU cache 的实现]
 - [tinyurl]

---

### 反转链表
#### 题目：
反转一个单链表。
#### Python Solution：
**分析：** 递归法和迭代法，而迭代法又分为了两种：头插法和尾插法。

```Python
class Solution:  # 递归法 找到最后两个节点调整顺序，向前递归。
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
```

```Python
class Solution:  # 迭代法 尾插法的简略写法。
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            pre, pre.next, head = head, pre, head.next
        return pre
```

```Python
class Solution:  # 迭代法 头插法，面试时需要配合画图和面试官讲解
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            cur = head.next
            head.next = cur.next
            cur.next = dummy.next
            dummy.next = cur
        return dummy.next
```

[返回目录](#00)

---

### 两个一组反转链表
#### 题目：
给定一个链表，每隔两个相邻节点交换一次并返回其头部。 您不能修改列表节点中的值，只能更改节点本身。
#### Python Solution：
**分析：** 配合上一道题的头插法食用更美味。

```Python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = tmp = ListNode(0)
        tmp.next = head
        while head and head.next:
            cur = head.next
            head.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            tmp, head = head, head.next
        return dummy.next
```

[返回目录](#01)

---

### k个一组反转链表
#### 题目：
给定一个链表，一次反转链表k的节点并返回其修改后的列表。

k是一个正整数，并且小于或等于链接列表的长度。如果节点数不是k的倍数，那么最后剩下的节点应保持原样。
#### Python Solution：
**分析：** 这是一道难度比较大的题，如果剩余反转的链表长度不足 k ，那么保持原样提示我们要对链表计数。用 while True 建立一个循环即可。

```Python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = tmp = ListNode(0)
        tmp.next = left = right = head
        while True:
            count = 0
            while count < k and right:
                count += 1
                right = right.next
            if count == k:
                pre, post = right, left
                for _ in range(k):
                    pre, pre.next, post = post, pre, post.next
                tmp.next, tmp, left = pre, left, right
            else:
                return dummy.next
```

[返回目录](#02)

---

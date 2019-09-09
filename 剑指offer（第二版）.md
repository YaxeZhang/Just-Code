<span id = "00">手机 Openhub 用户无法实现 Markdown 页内跳转，请点击右上角选择外部浏览器打开（已提交 Openhub issue...）</span>
# 剑指offer Python题解
   - [03.数组中重复的数字](#3数组中重复的数字)
   - [04.二维数组中的查找](#4二维数组中的查找)
   - [05.替换空格](#5替换空格)
   - [06.从尾到头打印链表](#6从尾到头打印链表)
   - [07.重建二叉树](#7重建二叉树)
   - [08.二叉树的下一个结点](#8二叉树的下一个结点)
   - [09.用两个栈实现队列](#9用两个栈实现队列)
   - [10.斐波那契数列](#10斐波那契数列)
   - [11.旋转数组中的最小数字](#11旋转数组中的最小数字)
   - [15.二进制中 1 的个数](#15二进制中-1-的个数)
   - [18.删除列表中重复的结点](#18删除列表中重复的结点)
   - [21.调整数组顺序使奇数位于偶数前面](#21调整数组顺序使奇数位于偶数前面)
   - [22.链表中倒数第 k 个结点](#22链表中倒数第-k-个结点)
   - [23.链表中环的入口结点](#23链表中环的入口结点)
   - [24.反转链表](#24反转链表)
   - [25.合并两个排序的链表](#25合并两个排序的链表)
   - [27.二叉树的镜像](#27二叉树的镜像)
   - [52.两个链表的第一个公共结点](#52两个链表的第一个公共结点)
   - [57.和为S的两个数](#57和为S的两个数)
   - [58.翻转字符串]()
   - [66.构建乘积数组](#66构建乘积数组)

### 3.数组中重复的数字

#### 题目描述

在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

#### 解法

```python
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False
        for i in range(len(numbers)):
            if numbers[i] >= len(numbers) or numbers[i] < 0:
                return False
            while numbers[i] != i:                      # 一直交换一直到 numbers[i] 等于 i
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    idx = numbers[i]
                    numbers[i], numbers[idx] = numbers[idx], numbers[i]
        return False
```

[回到目录](#00)

### 4.二维数组中的查找
#### 题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#### 解法：

```python
class Solution:
    def Find(self, target, array):
        if not array:
            return False
        row = len(array)                # 数组的行数
        col = len(array[0])             # 数组的列数
        i = row - 1
        j = 0                           # i, j这样规定是从左下开始查找，也可以从右上
        while i >= 0 and j < col:       # 双指针来判断是否在array中
            if array[i][j] == target:
                return True             # 如果等于输出True
            elif array[i][j] > target:
                i -= 1                  # 如果大于则往上移一格
            else:
                j += 1                  # 如果小于则往右移一格
        return False                    #如果最后走到了边界仍没有，则输出False
```

[回到目录](#00)

### 5.替换空格
#### 题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为 We Are Happy .则经过替换之后的字符串为 We%20Are%20Happy  。
#### 解法：

```python
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        res = ''
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                res += '02%'
            else:
                res += s[i]
        return res[::-1]
```

[回到目录](#00)

### 6.从尾到头打印链表
#### 题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
#### 解法：

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        res = []
        while listNode:
            res.insert(0, listNode.val)
            listNode = listNode.next
        return res
```

[回到目录](#00)

### 7.重建二叉树
#### 题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
#### 解法：

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(0)
        root.val = pre[0]
        idx = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1: idx + 1], tin[:idx])
        root.right = self.reConstructBinaryTree(pre[idx + 1:], tin[idx + 1:])
        return root
```

```python
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        def predfs(stop):
            if pre and tin[0] != stop:
                root = TreeNode(pre.pop(0))
                root.left = predfs(root.val)
                tin.pop(0)
                root.right = predfs(stop)
                return root
        tin, pre = tin[:], pre[:]
        return predfs(None)
```

[回到目录](#00)

### 8.二叉树的下一个结点
#### 题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
#### 解法：

```python
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):  # 这道题情况一定要考虑全
        if not pNode:
            return None
        if pNode.right:        # 如果有右结点，那么此时pNode是根结点，
                               # 下一个结点是右子树的最左边的结点
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        while pNode.next:      # 用来判断当前结点是不是根结点
            if pNode.next.left == pNode:
                               # 如果是左结点，那么返回它的父结点
                return pNode.next
            pNode = pNode.next # 如果不是，再向上找
        return pNode.next
```

[回到目录](#00)

### 9.用两个栈实现队列
#### 题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
#### 解法：

```python
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, node):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(node)
        while self.s2:
            self.s1.append(self.s2.pop())
    def pop(self):
        return self.s1.pop()
```

[回到目录](#00)

### 10.斐波那契数列
#### 题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
#### 解法：

```python
class Solution:
    def Fibonacci(self, n):
        if n <= 1:
            return n
        return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
```

```python
class Solution:
    def Fibonacci(self, n):
        res=[0, 1, 1]
        for _ in range(n - 2):
            res[0], res[1], res[2] = res[1], res[2], res[1] + res[2]
        return res[-1] if n > 2 else res[n]
```

```python
class Solution:
    def Fibonacci(self, n):
        a, b = 1, 0
        while n:
            b = a + b
            a = b - a
            n -= 1
        return b
```

[回到目录](#00)

### 11.旋转数组中的最小数字
#### 题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
#### 解法：

```python
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        i, j = 0, len(rotateArray) - 1
        while i + 1 < j:
            mid = int(i + (j - i) / 2)
            if rotateArray[mid] > rotateArray[j]:
                i = mid
            else:
                j = mid
        if rotateArray[i] <= rotateArray[j]:
            return rotateArray[i]
        else:
            return rotateArray[j]
```

[回到目录](#00)

### 15.二进制中 1 的个数
#### 题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
#### 解法：

```python
class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n &= 0xffffffff
        while n:
            count += 1
            n &= (n - 1)
        return count
```

[回到目录](#00)

### 18.删除列表中重复的结点
#### 题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
#### 解法：

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        dummy = tmp = ListNode(0)
        tmp.next = pHead
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                while pHead and pHead.next and pHead.val == pHead.next.val:
                    pHead = pHead.next
                tmp.next = pHead.next
                pHead = pHead.next
            else:
                tmp = tmp.next
                pHead = pHead.next
        return dummy.next
```

[回到目录](#00)

### 21.调整数组顺序使奇数位于偶数前面
#### 题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分。
#### 解法：

```python
class Solution:
    def reOrderArray(self, array):
        if not array:
            return None
        i, j = 0, len(array) - 1
        while i <= j:
            while i <= len(array) - 1 and array[i] % 2 == 1:
                i += 1
            while j >= 0 and array[j] % 2 == 0:
                j -= 1
            array[i], array[j] = array[j], array[i]
        return array
```

[回到目录](#00)

### 22.链表中倒数第 k 个结点
#### 题目描述
输入一个链表，输出该链表中倒数第k个结点。
#### 解法：

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <= 0:   # 判断条件head为空或者k<=0都不是常规满足的条件
            return None
        pre = post = head        # 快慢指针做这道题
        while k:                 # 快指针先走 k 步
            if pre:              # 加判断是防止 k 的数值比链表的长度长
                pre = pre.next
                k -= 1
            else:
                return None
        while pre:               # 快慢指针一起走，保持 k 个距离
            pre = pre.next
            post = post.next
        return post
```

[回到目录](#00)

### 23.链表中环的入口结点
#### 题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
#### 解法：

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next:
            return None
        pre = post = pHead
        while pre and pre.next:       # 确保快指针有意义没有到头
            post = post.next          # 慢指针走一步
            pre = pre.next.next       # 快指针走两步
            if pre == post:           # 相遇的时候即是有环
                post = pHead          # 慢指针再从头走
                while pre != post:    # 两个指针都是每次一步直到相遇
                    pre = pre.next
                    post = post.next
                return post           # 相遇的地方即是环的入口
        return None
```

[回到目录](#00)

### 24.反转链表
#### 题目描述
输入一个链表，反转链表后，输出新链表的表头。
#### 解法：

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre, cur = None, pHead
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
# 简化如下
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre, cur = None, pHead
        while cur:
            pre, pre.next, cur = cur, pre, cur.next
        return pre
# 递归法
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.ReverseList(pHead.next)
            pHead.next.next=pHead
            pHead.next=None
            return newHead
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

[回到目录](#00)

### 25.合并两个排序的链表
#### 题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
#### 解法：

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        dummy = tmp = ListNode(-1)  # 创建一个新链表来合并两个旧链表
        p1, p2 = pHead1, pHead2
        while p1 and p2:            # 都不为空的情况
            if p1.val <= p2.val:
                tmp.next = p1
                p1 = p1.next
            else:
                tmp.next = p2
                p2 = p2.next
            tmp = tmp.next
        tmp.next = p1 or p2         # 一开始都为空或者其中一个为空或者经过while循环后其中一个为空的情况都包含了
        return dummy.next
```

[回到目录](#00)

### 27.二叉树的镜像
#### 题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
#### 输入描述

```python
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
```

#### 解法：

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        if root.left:                # 简洁的话可以不加下面这两个判断，
            self.Mirror(root.left)   # 因为递归调用后第一个判断和这个等效，
        if root.right:               # 但是涉及函数调用，会让速度更慢
            self.Mirror(root.right)
        return root
```

[回到目录](#00)

### 52.两个链表的第一个公共结点
#### 题目描述
输入两个链表，找出它们的第一个公共结点。
#### 解法：

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        l1, l2 = 0, 0
        p1, p2 = pHead1, pHead2
        while p1:
            p1 = p1.next
            l1 += 1
        while p2:
            p2 = p2.next
            l2 += 1
        p1, p2 = pHead1, pHead2
        if l1 >= l2:
            while l1 - l2:
                p1 = p1.next
                l1 -= 1
        else:
            while l2 - l1:
                p2 = p2.next
                l2 -= 1
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None
```

```python
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1, p2 = pHead1, pHead2
        while p1 != p2:          # 1.判断是否为同一个相交处 2.判断是否走完了一整遍
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1
```

[回到目录](#00)

### 57.和为S的两个数
#### 题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
#### 解法：

```python
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        i = 0
        j = len(array) - 1
        while i < j:
            if array[i] + array[j] > tsum:
                j -= 1
            elif array[i] + array[j] < tsum:
                i += 1
            else:
                return array[i], array[j]
        return []
```
##### 57 - 1.和为S的连续正数序列
###### 题目描述
输入一个正数s,打印出所有和为s的连续正数序列（至少含有两个数）。例如输入15，由于1+2+3+4+5=4+5+6=7+8=15；所以打印出三个连续序列1 ~ 5, 4 ~ 6, 7 ~ 8
###### 解法：

```python
class Solution:
    def FindContinuousSequence(self, tsum):
        low, high = 1, 2
        res = []
        while low <= tsum // 2:
            if sum(range(low, high + 1)) == tsum:
                res.append(list(range(low, high + 1)))
                low += 1
            elif sum(range(low, high + 1)) < tsum:
                high += 1
            else:
                low += 1
        return res
```

[回到目录](#00)

### 66.构建乘积数组
#### 题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
#### 解法：

```python
class Solution:
    def multiply(self, A):
        B = [1] * len(A)
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i- 1]
        tmp = 1
        for j in range(len(A) - 2, -1, -1):
            tmp *= A[j + 1]
            B[j] *= tmp
        return B
```

[回到目录](#00)

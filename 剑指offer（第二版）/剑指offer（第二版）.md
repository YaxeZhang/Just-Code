<span id = "00">手机 Openhub 用户无法实现 Markdown 页内跳转，请点击右上角选择外部浏览器打开（已提交 Openhub issue...）</span>
# 剑指offer Python题解
   - [03.数组中重复的数字](#3数组中重复的数字)
   - [04.二维数组中的查找](#4二维数组中的查找)
   - [05.替换空格](#5替换空格)
   - [06.从尾到头打印链表](#6从尾到头打印链表)
   - [07.重建二叉树](#7重建二叉树)
   - [08.二叉树的下一个节点](#8二叉树的下一个节点)
   - [09.用两个栈实现队列](#9用两个栈实现队列)
   - [10.斐波那契数列](#10斐波那契数列)
   - [11.旋转数组中的最小数字](#11旋转数组中的最小数字)
   - [12.矩阵中的路径]
   - [13.机器人的运动范围](#13机器人的运动范围)
   - [14.剪绳子](#14剪绳子)
   - [15.二进制中 1 的个数](#15二进制中-1-的个数)
   - [16.数值的整数次方](#16数值的整数次方)
   - [17.打印从1到最大的n位数]
   - [18.删除列表中重复的节点](#18删除列表中重复的节点)
   - [19.正则表达式匹配]
   - [20.表示数值的字符串]
   - [21.调整数组顺序使奇数位于偶数前面](#21调整数组顺序使奇数位于偶数前面)
   - [22.链表中倒数第 k 个节点](#22链表中倒数第-k-个节点)
   - [23.链表中环的入口节点](#23链表中环的入口节点)
   - [24.反转链表](#24反转链表)
   - [25.合并两个排序的链表](#25合并两个排序的链表)
   - [26.树的子结构](#26树的子结构)
   - [27.二叉树的镜像](#27二叉树的镜像)
   - [28.对称的二叉树](#28对称的二叉树)
   - [29.顺时针打印矩阵](#29顺时针打印矩阵)
   - [30.包含min函数的栈](#30包含min函数的栈)
   - [31.栈的压入弹出序列](#31栈的压入弹出序列)
   - [32.从上到下打印二叉树](#32从上到下打印二叉树)
   - [33.二叉搜索树的后序遍历序列](#33二叉搜索树的后序遍历序列)
   - [34.二叉树中和为某一值的路径](#34二叉树中和为某一值的路径)
   - [35.复杂链表的复制](#35复杂链表的复制)
   - [36.二叉搜索树与双向链表](#36二叉搜索树与双向链表)
   - [37.序列化二叉树](#37序列化二叉树)
   - [38.字符串的排列]
   - [39.数组中出现次数超过一半的数字](#39数组中出现次数超过一半的数字)
   - [40.最小的k个数]
   - [41.数据流的中位数]
   - [42.连续子数组的最大和](#42连续子数组的最大和)
   - [43.1~n整数中1出现的次数]
   - [44.数字序列中某一位的数字]
   - [45.把数组排成最小的数](#45把数组排成最小的数)
   - [46.把数字翻译成字符串](#46把数字翻译成字符串)
   - [47.礼物的最大价值](#47礼物的最大价值)
   - [48.最长不含重复字符的子字符串](#48最长不含重复字符的子字符串)
   - [49.丑数](#49丑数)
   - [50.第一个只出现一次的字符](#50第一个只出现一次的字符)
   - [51.数组中的逆序对]
   - [52.两个链表的第一个公共节点](#52两个链表的第一个公共节点)
   - [53.在排序数组中查找数字](#53在排序数组中查找数字)
   - [54.二叉搜索树的第k个结点](#54二叉搜索树的第k个结点)
   - [55.二叉树的深度](#55二叉树的深度)
   - [56.数组中数字出现的次数](#56数组中数字出现的次数)
   - [57.和为S的两个数](#57和为S的两个数)
   - [58.翻转字符串](#58翻转字符串)
   - [59.队列的最大值](#59队列的最大值)
   - [60.n个骰子的点数]
   - [61.扑克牌中的顺子](#61扑克牌中的顺子)
   - [62.圆圈中最后剩下的数字](#62圆圈中最后剩下的数字)
   - [63.股票的最大利润](#63股票的最大利润)
   - [64.求 1+2+3+...+n]
   - [65.不用加减乘除做加法](#65不用加减乘除做加法)
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
        for _, v in enumerate(numbers):
            if v >= len(numbers) or v < 0:
                return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    idx = numbers[i]
                    numbers[i], numbers[idx] = numbers[idx], numbers[i]
        return False
```

**使用 O(1) 空间的解法:** 但条件一定要明确，存在重复数字。思维类似于寻找链表环的入口。

```python
class Solution:
    def duplicateInArray(self, nums):
        f = s = 0
        while f == 0 or f != s:
            f = nums[nums[f]]
            s = nums[s]
        f = 0
        while f != s:
            f = nums[f]
            s = nums[s]
        return s
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
        i， j = row - 1, 0                           # i, j这样规定是从左下开始查找，也可以从右上
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
        res = []
        for i in s:
            if i == ' ':
                res.extend(['%', '2', '0'])
            else:
                res.append(i)
        return ''.join(res)
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
    def printListFromTailToHead(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]
```

**还可以递归实现：**

```python
class Solution:
    def printListReversingly(self, head):
        self.res = []

        def helper(p):
            if p:
                helper(p.next)
                self.res.append(p.val)

        helper(head)
        return self.res
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
    def buildTree(self, preorder, inorder):

        def dfs(stop):
            if preorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = dfs(root.val)
                inorder.pop()
                root.right = dfs(stop)
                return root

        preorder, inorder = preorder[::-1], inorder[::-1]
        return dfs(None)
```

[回到目录](#00)

### 8.二叉树的下一个节点
#### 题目描述
给定一个二叉树和其中的一个节点，请找出中序遍历顺序的下一个节点并且返回。注意，树中的节点不仅包含左右子节点，同时包含指向父节点的指针。
#### 解法：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.father = None
class Solution:
    def inorderSuccessor(self, q):
        if not q: return None
        if q.right:
            q = q.right
            while q.left:
                q = q.left
            return q
        while q.father and q.father.right == q:
            q = q.father
        return q.father
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
        for _ in range(n):
            res[0], res[1], res[2] = res[1], res[2], res[1] + res[2]
        return res[0] if n > 2 else res[n]
```

```python
class Solution:
    def Fibonacci(self, n):
        a, b = 1, 0
        for _ in range(n):
            a, b = a+b, a
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
    def findMin(self, nums):
        if not nums: return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] == nums[r]:
                r -= 1
            else:
                r = mid
        return nums[l]
```

[回到目录](#00)

### 13.机器人的运动范围
#### 题目描述
地上有一个 m 行和 n 列的方格，横纵坐标范围分别是 0∼m−1 和 0∼n−1。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格。但是不能进入行坐标和列坐标的数位之和大于 k 的格子。请问该机器人能够达到多少个格子？
#### 解法：

```python
class Solution:
    def movingCount(self, threshold, rows, cols):

        def dfs(x, y):
            if 0<=x<rows and 0<=y<cols and not dp[x][y]:
                dp[x][y] = 1
                if threshold >= sum(map(int, list(str(x)) + list(str(y)))):
                    self.res += 1
                    for dx, dy in delta:
                        dfs(x+dx, y+dy)

        dp = [[0] * cols for _ in range(rows)]
        self.res = 0
        delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
        dfs(0, 0)
        return self.res
```

[回到目录](#00)

### 14.剪绳子
#### 题目描述
给你一根长度为 n 绳子，请把绳子剪成 m 段（m、n 都是整数，2≤n≤58 并且 m≥2）。每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]k[1] … k[m] 可能的最大乘积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到最大的乘积18。
#### 解法：

```python
class Solution:
    def maxProductAfterCutting(self,n):
        dp = [0]*(n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], max(dp[j]*(i-j), j*(i-j)))
        return dp[n]
```

```python
class Solution:
    def maxProductAfterCutting(self,n):
        return n - 1 if n < 4 else 3 ** ((n-2) // 3) * ((n-2) % 3 + 2)
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

### 16.数值的整数次方
#### 题目描述
实现函数double Power(double base, int exponent)，求base的 exponent次方。不得使用库函数，同时不需要考虑大数问题。
#### 解法：

```python
class Solution:  # 简单快速幂解法
    def Power(self, base, exponent):
        exp = abs(exponent)
        r = 1
        while exp:
            if exp & 1:
                r *= base
            base *= base
            exp >>= 1
        return r if exponent >= 0 else 1/r
```

[回到目录](#00)

### 18.删除列表中重复的节点
#### 题目描述
在一个排序的链表中，存在重复的节点，请删除该链表中重复的节点，重复的节点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
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
                while pHead.next and pHead.val == pHead.next.val:
                    pHead = pHead.next
                tmp.next = pHead.next
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

### 22.链表中倒数第 k 个节点
#### 题目描述
输入一个链表，输出该链表中倒数第k个节点。
#### 解法：

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findKthToTail(self, head, k):
        if not head or k <= 0:
            return None
        fast = slow = head
        for _ in range(k): # 快慢指针来走，之所以先判断是为了防止 k 等于链表长度的情况。
            if not fast: return None
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        return slow
```

[回到目录](#00)

### 23.链表中环的入口节点
#### 题目描述
给一个链表，若其中包含环，请找出该链表的环的入口节点，否则，输出null。
#### 解法：

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
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
            pHead.next.next = pHead
            pHead.next = None
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

### 26.树的子结构
#### 题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。我们规定空树不是任何树的子结构。
#### 解法：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasSubtree(self, p1, p2):
        if not p1 or not p2:
            return False
        if self.isPart(p1, p2):
            return True
        return self.hasSubtree(p1.left, p2) or self.hasSubtree(p1.right, p2)

    def isPart(self, p1, p2):
        if not p2:
            return True
        if not p1 or p1.val != p2.val:
            return False
        return self.isPart(p1.left, p2.left) and self.isPart(p1.right, p2.right)
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

### 28.对称的二叉树
#### 题目描述
请实现一个函数，用来判断一棵二叉树是不是对称的。

如果一棵二叉树和它的镜像一样，那么它是对称的。
#### 输入描述

```golang
如下图所示二叉树[1,2,2,3,4,4,3,null,null,null,null,null,null,null,null]为对称二叉树：
    1
   / \
  2   2
 / \ / \
3  4 4  3

如下图所示二叉树[1,2,2,null,4,4,3,null,null,null,null,null,null]不是对称二叉树：
    1
   / \
  2   2
   \ / \
   4 4  3
```

#### 解法：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root: return True

        def isSym(p, q):
            if p and q:
                return p.val == q.val and isSym(p.left, q.right) and isSym(p.right, q.left)
            return p is q

        return isSym(root.left, root.right)
```

[回到目录](#00)

### 29.顺时针打印矩阵
#### 题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#### 解法：

```python
class Solution:
    def printMatrix(self, matrix):
        res = []
        if not matrix: return res
        x = y = i = 0
        delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
        pos = [0, 0, len(matrix[0])-1, len(matrix)-1] # 左、上、右、下。后面懒得判断推出来的。
        while pos[0] <= pos[2] and pos[1] <= pos[3]:
            while pos[0] <= y <= pos[2] and pos[1] <= x <= pos[3]:
                res.append(matrix[x][y])
                x, y = x+delta[i][0], y+delta[i][1]
            x, y = x-delta[i][0], y-delta[i][1]
            i = (i+1) % 4
            pos[i] += sum(delta[i])
            x, y = x+delta[i][0], y+delta[i][1]
        return res
```

**动用了hin多空间**

```python
class Solution:
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix[0]
            matrix = list(zip(*matrix[1:]))[::-1]
        return res
```

[回到目录](#00)

### 30.包含min函数的栈
#### 题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
#### 解法：

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.stkmin = []

    def push(self, x: int) -> None:
        if not self.stkmin or self.getMin() > x:
            self.stkmin.append(x)
        else:
            self.stkmin.append(self.getMin())
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            self.stkmin.pop()
            return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stkmin:
            return self.stkmin[-1]
```

**进阶牛逼版 O(1)空间复杂度 O(1)时间复杂度**

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = 0

    def push(self, x: int) -> None:
        if not self.stack:
            self.mins = x
            self.stack.append(0)
        else:
            compare = x - self.mins
            self.stack.append(compare)
            self.mins = x if compare < 0 else self.mins            

    def pop(self) -> None:
        top1 = self.stack.pop()
        if top1 < 0:
            self.mins = self.mins - top1

    def top(self) -> int:
        if self.stack[-1] > 0:
            return self.mins + self.stack[-1]
        else:
            return self.mins

    def getMin(self) -> int:
        return self.mins
```

[回到目录](#00)

### 31.栈的压入弹出序列
#### 题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。

假设压入栈的所有数字均不相等。

例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。

注意：若两个序列长度不等则视为并不是一个栈的压入、弹出序列。若两个序列都为空，则视为是一个栈的压入、弹出序列。
#### 解法：

```python
class Solution:
    def isPopOrder(self, pushV, popV):
        if len(pushV) != len(popV): return False
        stack, i = [], 0       # 用 stack 来模拟进出栈。
        for v in pushV:
            stack.append(v)
            while stack and stack[-1] == popV[i]:
                stack.pop()
                i += 1
        return not stack
```

[回到目录](#00)

### 32.从上到下打印二叉树
#### 题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
#### 解法：

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        res = []
        if root:
            level = [root]
            while level:
                res.extend([x.val for x in level])
                level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return res
```

[回到目录](#00)

### 33.二叉搜索树的后序遍历序列
#### 题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true，否则返回false.假设输入的数组的任意两个数字都互不相同。
#### 解法：

```python
class Solution:
    def verifySequenceOfBST(self, sequence):
        if not sequence:
            return True  # 看 OJ 要求 True or False
        def dfs(Max, stop):
            if sequence and Max >= sequence[-1] >= stop:
                x = sequence.pop()
                dfs(Max, x)
                dfs(x, stop)
        dfs(float('inf'), float('-inf'))
        return not sequence
```

[回到目录](#00)

### 34.二叉树中和为某一值的路径
#### 题目描述
输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
#### 解法：
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, tsum: int) -> List[List[int]]:
        if not root :
            return []

        temp, res = [], []

        def DFTS(root):
            temp.append(root.val)
            if not root.left and not root.right and sum(temp) == tsum:
                res.append(temp.copy())
            if root.left:
                DFTS(root.left)
            if root.right:
                DFTS(root.right)
            temp.pop()

        DFTS(root)
        return res
```

**迭代法**

```python
class Solution:
    def pathSum(self, root: TreeNode, Psum: int) -> List[List[int]]:
        if not root:
            return []
        stack, res = [(root, [root.val])], []
        while stack:
            node, cur = stack.pop()
            if not node.left and not node.right and sum(cur) == Psum:
                res.append(cur)
            if node.left:
                stack.append((node.left, cur + [node.left.val]))
            if node.right:
                stack.append((node.right, cur + [node.right.val]))
        return res
```

[返回目录](#00)

### 35.复杂链表的复制
#### 题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
#### 解法：

```python
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        p1 = p2 = p3 = pHead
        while p1:
            tmp = RandomListNode(p1.label)
            tmp.next = p1.next
            tmp.random = None
            p1.next = tmp
            p1 = p1.next.next
        while p2:
            tmp = p2.next
            tmp.random = p2.random.next if p2.random else None
            p2 = p2.next.next
        dummy = tmp = p3.next
        while p3:
            p3.next = p3.next.next
            tmp.next = p3.next.next if p3.next else None
            p3, tmp = p3.next, tmp.next
        return dummy
```

[回到目录](#00)

### 36.二叉搜索树与双向链表
#### 题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
注意：需要返回双向链表最左侧的节点。
#### 解法：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convert(self, root):
        if not root: return None
        prev = None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            node.left = prev
            if prev:
                prev.right = node
            root = node.right
            prev = node
        cur = prev
        while cur.left:
            cur = cur.left
        return cur
```

[回到目录](#00)

### 37.序列化二叉树
#### 题目描述
请实现两个函数，分别用来序列化和反序列化二叉树。
您需要确保二叉树可以序列化为字符串，并且可以将此字符串反序列化为原始树结构。
#### 解法：

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ','.join(vals)


    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split(','))
        return doit()

```

[返回目录](#00)

### 39.数组中出现次数超过一半的数字
#### 题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
#### 解法：

```python
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        candidate = numbers[0]
        count = 1
        for i in range(1,len(numbers)):
            if numbers[i] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = numbers[i]
                    count = 1
        # 上面是摩尔投票法，下面为验证，这样可以保证时间复杂度在 O(n) 。
        if numbers.count(candidate) * 2 > len(numbers):
            return candidate
        else:
            return 0
```

[回到目录](#00)

### 42.连续子数组的最大和
#### 题目描述
一个整数数组中的元素有正有负，在该数组中找出一个连续子数组，要求该连续子数组中各元素的和最大，这个连续子数组便被称作最大连续子数组。比如数组{2,4,-7,5,2,-1,2,-4,3}的最大连续子数组为{5,2,-1,2}，最大连续子数组的和为5+2-1+2=8。
#### 解法：

```python
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        best = cur = array[0]
        for i in range(1, len(array)):
            cur = max(array[i], array[i] + cur)
            best = max(best, cur)
        return best
```

[回到目录](#00)

### 45.把数组排成最小的数
#### 题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组[3, 32, 321]，则打印出这3个数字能排成的最小数字321323。
#### 解法：

```python
class Solution:
    def printMinNumber(self, nums):
        if not nums: return ''
        if set(nums) == {0}: return "0"
        diff = len(str(max(nums))) - len(str(min(nums))) + 1
        return "".join(sorted(map(str,nums),key= lambda x: x*diff))
```

[回到目录](#00)

### 46.把数字翻译成字符串
#### 题目描述
给定一个数字，我们按照如下规则把它翻译为字符串：
0翻译成”a”，1翻译成”b”，……，11翻译成”l”，……，25翻译成”z”。
一个数字可能有多个翻译。例如12258有5种不同的翻译，它们分别是”bccfi”、”bwfi”、”bczi”、”mcfi”和”mzi”。
请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。
#### 解法：

```python
class Solution:
    def getTranslationCount(self, s):
        if not s: return 0
        dp = [1] * len(s)
        for i in range(len(s)-2, -1, -1):
            dp[i] = dp[i+1]
            if s[i] == '1' or s[i] == '2' and s[i+1] < '6':
                dp[i] += dp[i+2]
        return dp[0]
```

**可简化为 O(1) 空间**

```python
class Solution:
    def getTranslationCount(self, s):
        if not s: return 0
        l = r = 1
        for i in range(len(s)-2, -1, -1):
            if s[i] == '1' or s[i] == '2' and s[i+1] < '6':
                l, r = l + r, l
            else:
                r = l
        return l
```

[回到目录](#00)

### 47.礼物的最大价值
#### 题目描述
在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？
#### 解法：

```python
class Solution:
    def getMaxValue(self, grid):
        dp = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j > 0:
                    dp[j] = grid[i][j] + max(dp[j-1], dp[j])
                else:
                    dp[j] = grid[i][j] + dp[j]
        return dp[-1]
```

[回到目录](#00)

### 48.最长不含重复字符的子字符串
#### 题目描述
给定一个字符串，找到最长子字符串的长度而不重复字符。
#### 解法：
**分析：** 滑动窗口解决问题，如果遍历一遍 s，如果遍历到没有出现的元素，窗口右端立马扩张，并计算最大长度。如果遍历到之前出现的元素，则将窗口左端置为上次出现的位置的后一位。只有出现没有遍历过的元素才会计算最大长度。因为一旦是遍历过的元素，只有可能是保持不变或者缩小。

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        used = {}
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            used[c] = i
        return maxLength
```

[返回目录](#00)

### 49.丑数
#### 题目描述
我们把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。求第n个丑数的值。
#### 解法：

```python
class Solution:
    def nthUglyNumber(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]
```

```python
class Solution:
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n):
        return self.ugly[n-1]
```

[回到目录](#00)

### 50.第一个只出现一次的字符
#### 题目描述
在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出b。如果字符串中不存在只出现一次的字符，返回#字符。
#### 解法：

```python
class Solution:
    def firstNotRepeatingChar(self, s):
        if not s: return '#'
        import collections
        count = collections.Counter(s)
        for i in set(s):
            if count[i] == 1:
                return i
        return '#'
```

[回到目录](#00)

### 52.两个链表的第一个公共节点
#### 题目描述
输入两个链表，找出它们的第一个公共节点。
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

### 53.在排序数组中查找数字
#### 题目描述
统计一个数字在排序数组中出现的次数。如果不存在返回 0。
例如输入排序数组[1, 2, 3, 3, 3, 3, 4, 5]和数字3，由于3在这个数组中出现了4次，因此输出4。
#### 解法：

```python
class Solution:
    def getNumberOfK(self, nums, k):
        if not nums: return 0
        def search(lo, hi):
            if nums[lo] == k == nums[hi]:
                return [lo, hi]
            if nums[lo] <= k <= nums[hi]:
                mid = (lo + hi) // 2
                l, r = search(lo, mid), search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        l, r = search(0, len(nums)-1)
        return 0 if l == -1 else r - l + 1
```

[回到目录](#00)

### 54.二叉搜索树的第k个结点
#### 题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。

你可以假设树和k都存在，并且1≤k≤树的总结点数。
#### 解法：

```python
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthNode(self, root, k):
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            k -= 1
            if not k: return node
            root = node.right
          return None
```

[回到目录](#00)

### 55.二叉树的深度
#### 题目描述
输入一棵二叉树，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
#### 解法：

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        depthleft = self.TreeDepth(pRoot.left)
        depthright = self.TreeDepth(pRoot.right)
        return max(depthleft, depthright) + 1
```

[回到目录](#00)

### 56.数组中数字出现的次数
### 56-1.数组中只出现一次的两个数字
#### 题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。你可以假设这两个数字一定存在。
#### 解法：

```python
import functools
class Solution:
    def findNumsAppearOnce(self, nums):
        if len(nums) < 2: return []
        diff = functools.reduce(lambda r, x: r ^ x, nums)
        idx = len(bin(diff)) - bin(diff).rfind('1') - 1
        num1 = num2 = 0
        for num in nums:
            if (num >> idx) & 1:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
```

[回到目录](#00)

### 56-2.数组中唯一只出现一次的数字
#### 题目描述
在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。你可以假设满足条件的数字一定存在。
思考题：
如果要求只使用 O(n) 的时间和额外 O(1) 的空间，该怎么做呢？
#### 解法：

```python
class Solution:  # 面试用装x解法
    def findNumberAppearingOnce(self, nums):
        a = b = 0
        for n in nums:
            a = (a ^ n) & ~b
            b = (b ^ n) & ~a
        return a
```

```python
class Solution:  # 常规解法
    def findNumberAppearingOnce(self, nums):
        ans = 0
        for i in range(32):
            cnt = 0
            for n in nums:
                if (n >> i) & 1:
                    cnt += 1
            if cnt % 3:
                ans |= 1 << i
        return ans if ans < 2**31 else ans - 2**32
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

### 58.翻转字符串
#### 题目描述
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串“I am a student.”，则输出“student. a am I”
#### 解法：

```python
class Solution:
    def ReverseSentence(self, s):
        return ' '.join(s.split(' ')[::-1])
```

[回到目录](#00)

### 59.队列的最大值
#### 题目描述
给定一个数组和滑动窗口的大小，请找出所有滑动窗口的最大值。例如，输入数组{2,3,4,2,6,2,5,1}和数字3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}。
#### 解法：

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()             # 使用双向队列解决本题
        res = []
        for i, v in enumerate(nums):
            while dq and nums[dq[-1]] < v:   # dq中如果存在多个元素
                dq.pop()                     # 一定是降序排列的
            dq += i,
            if dq[0] == i - k:               # 判断dq中第一位是否有效
                dq.popleft()
            if i >= k - 1:                   # 满足滑动窗口长度才有输出
                res += nums[dq[0]],
        return res
```

[回到目录](#00)

### 61.扑克牌中的顺子
#### 题目描述
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，大小王可以看做任意数字。为了方便，大小王均以0来表示，并且假设这副牌中大小王均有两张。
#### 解法：

```python
class Solution:
    def isContinuous(self, numbers):
        if not numbers: return False
        nums = [x for x in numbers if x]
        return max(nums) - min(nums) < 5 if len(nums) == len(set(nums)) else False
```

[回到目录](#00)

### 62.圆圈中最后剩下的数字
#### 题目描述
题目：0,1,...,n-1这n个数字拍成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里身下的最后一个数字。
#### 解法：

**递归法** 代码不好理解并且递归深度大，不推荐。在牛客网上无法 AC 。但思路正确。

```python
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        return 0 if n == 1 else (self.LastRemaining_Solution(n - 1, m) + m) % n
```

**循环迭代法**

```python
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2,n + 1):
            last = (last + m) % i
        return last
```

[回到目录](#00)

### 63.股票的最大利润
#### 题目描述
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。
#### 解法：

```python
class Solution:
    def maxProfit(self, prices):
        min_p, max_p = float('inf'), 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p
```

[回到目录](#00)

### 65.不用加减乘除做加法
#### 题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用四则运算符号。
#### 解法：

```python
class Solution:
    def Add(self, num1, num2):
        mask = 0xffffffff    # 因为 Python 没有整型溢出，所以需要规定个范围掩码
        while num2 & mask:   # 当 num2 超过 mask 时，num1 也要和 mask 做 与
            num1, num2 = num1 ^ num2, (num1 & num2) << 1
        return num1 & mask if num2 > mask else num1
```

[回到目录](#00)

### 66.构建乘积数组
#### 题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]* A[1]* ...* A[i-1]* A[i+1]* ...* A[n-1]。不能使用除法。
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

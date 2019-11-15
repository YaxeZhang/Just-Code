

简化路径 #71
python 装饰器

洗牌算法
出现次数超过一半的数字
LC #862
8皇后
区间合并问题

## 链表
 - [反转链表](#反转链表)<span id = "101"></span>
 - [反转部分链表](#反转部分链表)<span id = "102"></span>
 - [两个一组反转链表](#两个一组反转链表)<span id = "103"></span>
 - [k个一组反转链表](#k个一组反转链表)<span id = "104"></span>
 - [奇偶次序分离后合并有序链表](#奇偶次序分离后合并有序链表)<span id = "105"></span>
 - [两个链表求和](#两个链表求和)<span id = "106"></span>

## 二叉树
 - [二叉树的前序中序后序遍历](#二叉树的前序中序后序遍历)<span id = "201"></span>
 - [重建二叉树](#重建二叉树)<span id = "202"></span>
 - [二叉树的翻转](#二叉树的翻转)<span id = "203"></span>
 - [二叉树的深度](#二叉树的深度)<span id = "204"></span>
 - [平衡二叉树](#平衡二叉树)<span id = "205"></span>
 - [二叉树的最大路径和](#二叉树的最大路径和)<span id = "206"></span>
 - [二叉树的最低公共祖先](#二叉树的最低公共祖先)<span id = "207"></span>

## 动态规划
 - [独特的路径](#独特的路径)<span id = "301"></span>
 - [House robber](#house-robber)<span id = "302"></span>
 - [换硬币]
 - [买卖股票的最佳时机I]
 - [买卖股票的最佳时机II]
 - [矩阵中的路径 jzoffer]
 - [正则表达式匹配 jzoffer]
 - [背包问题动态规划]
 - [子数组之和的最大值]
 - [最长不重复子串]
 - [矩阵中最长递增子序列  LC #329]

## 二分查找
 - [数字在数组中的位置 jzoffer]
 - [排序数组进行二分查找，平移后的排序数组进行二分查找 #33]

## 排序算法
 - [冒泡排序](#冒泡排序)<span id = "501"></span>
 - [快速排序]
 - [归并排序]
 - [堆排序]
 - [桶排序]

## 双指针
 - [Two Sum]
 - [3 Sum]
 - [3 Sum Closest]
 - [搜索二维矩阵]
 - [装满水的容器LC#11]

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
        return newhead
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

[返回目录](#101)

---

### 反转部分链表
#### 题目：
将链接列表从位置m反向到n。一次性完成。 注意：1≤m≤n≤列表长度。
#### Python Solution：
**分析：** 配合上一道题的头插法食用更美味。写起来更简洁，比尾插法好很多。

```Python
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = post = ListNode(0)
        post.next = pre = head
        for _ in range(m-1):
            post, pre = pre, pre.next
        for _ in range(n-m):
            cur = pre.next
            pre.next = cur.next
            cur.next = post.next
            post.next = cur
        return dummy.next
```

[返回目录](#102)

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

[返回目录](#103)

---

### k个一组反转链表
#### 题目：
给定一个链表，一次反转链表k的节点并返回其修改后的列表。

k是一个正整数，并且小于或等于链接列表的长度。如果节点数不是k的倍数，那么最后剩下的节点应保持原样。
#### Python Solution：
**分析：** 这是一道难度比较大的题，也可以看作是上一题的延伸。可以继续头插法，也可以尾插法，不过尾插法找结点要绕一点，归根结底是一样的 !!! 不过要注意的是循环 头插法 k-1 次，尾插法 k 次。如果剩余反转的链表长度不足 k ，那么保持原样提示我们要对链表计数。用 while True 建立一个循环即可。

```Python
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
                for _ in range(k-1):   # 这个 k-1 很关键。
                    cur = left.next
                    left.next = cur.next
                    cur.next = tmp.next
                    tmp.next = cur
                tmp, left = left, right
            else:
                return dummy.next
```

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

[返回目录](#104)

---

### 奇偶次序分离后合并有序链表
#### 题目：
给定一个链表，次序为奇数的节点按升序排列，次序为偶数的节点按降序排列，请返回排序好的有序链表。
#### Python Solution：
**分析：** 这道题比较有意思，乍一看很复杂但是思路十分清晰，分为三步：1. 奇偶次序分离链表 2. 将分离后降序的链表进行反转 3. 合并两个有序链表并返回。

```Python
class Solution:
    def reverseUpdate(self, head: ListNode) -> ListNode:
        if not head:                  # 首先对与链表进行判断
            return None

        oddhead = odd = head          # 进行第一步：奇偶次序分离
        evenhead = even = odd.next
        while even and even.next:
            odd.next = odd = even.next
            even.next = even = odd.next

        rev = None                    # 对降序的偶数次链表进行反转
        while evenhead:
            rev, rev.next, evenhead = evenhead, rev, evenhead.next

        dummy = tmp = ListNode(0)     # 合并两个有序链表
        tmp.next = oddhead
        while rev and oddhead:
            if rev.val > oddhead.val:
                tmp.next = oddhead
                oddhead = oddhead.next
            else:
                tmp.next = rev
                rev = rev.next
            tmp = tmp.next
        tmp.next = rev or oddhead
        return dummy.next
```

[返回目录](#105)

---

### 两个链表求和
#### 题目：
给定一个链表，次序为奇数的节点按升序排列，次序为偶数的节点按降序排列，请返回排序好的有序链表。
#### Python Solution：
**分析：** 有两种做法，一种是不用额外空间的做法，在原有的一个链表的基础上加，但是考虑的边界条件等比较多，不推荐，如果面试官没有要求尽量用第二种：计算两个链表代表的数，相加后新创建一个链表。

```Python
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

**麻烦的 O(1) 空间的做法如下，不关心可跳过：**

```Python
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

[返回目录](#106)

---

### 二叉树的前序中序后序遍历
#### 题目：
给定一个二叉树，给出它的前序、中序、后序遍历，递归和非递归方式。
#### Python Solution：
**分析：** 这是二叉树最基本的一道题，也是考察对二叉树的认识和递归的题。后序遍历的非递归有点难度，但是也可以取巧。

```Python
class Solution: # 前序遍历
    def preorderTraversal(self, root):
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

class Solution:
    def preorderTraversal(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
```

```Python
class Solution: # 中序遍历
    def inorderTraversal(self, root):
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

class Solution:
    def inorderTraversal(self, root):
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res
```

```Python
class Solution: # 后序遍历
    def postorderTraversal(self, root):
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

class Solution:
    def postorderTraversal(self, root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]
```

[返回目录](#201)

---

### 重建二叉树
#### 题目：
给定一棵树的后序和中序（前序和中序）遍历，构造二叉树。
注意： 您可以假定树中不存在重复项
#### Python Solution：
**分析：** 以后序中序为例进行解析，推荐 dfs 那种，效率更高。两种解法都非常好理解，第一种是找到根节点，然后将 inorder 查分为两半继续寻找，问题在于如何找到 根节点在 inorder 的位置，下面第一种解法有点傻，更高效的是建立一个哈希表，占用 O(n) 的空间、查询时间为O(1)。第二种解法呢则非常聪明，不用找根节点的位置，构建 root.right 时每次都调用的是 postorder 最后一个元素，终点是 root.val 。构建 root.right 的时候终点是 None。

```Python
class Solution:  # 推荐解法，可以和面试官讲解思路，赞！
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def postdfs(stop):
            if postorder and inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = postdfs(root.val)
                inorder.pop()
                root.left = postdfs(stop)
                return root
        return postdfs(None)

class Solution:  # 常规解法，中规中矩但条件判断易出现问题。
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root
```

```Python
class Solution:  # 常规写法差不多不写了，理解下递归左右子节点的顺序。
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def predfs(stop):
            if preorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = predfs(root.val)
                inorder.pop()
                root.right = predfs(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return predfs(None)
```

[返回目录](#202)

---

### 二叉树的翻转
#### 题目描述
左右翻转二叉树。
#### Python Solution：
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
```

**迭代法**

```python
class Solution:
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])
        return root
```

[返回目录](#203)

---

### 二叉树的深度
#### 题目描述
输入一棵二叉树，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
#### Python Solution：
**分析：** 简单题，递归求解即可，写好 base case，不过迭代也可以做，就是一般的 dfs 或者 bfs 。

```Python
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        depthleft = self.TreeDepth(pRoot.left)
        depthright = self.TreeDepth(pRoot.right)
        return max(depthleft, depthright) + 1
```

[返回目录](#204)

---

### 平衡二叉树
#### 题目描述
给定一棵二叉树，确定它是否是高度平衡的。对于此问题，将高度平衡的二叉树定义为： 一棵二叉树，其中每个节点的两个子树的深度相差不超过1。
#### Python Solution：
**分析：** 上一道题二叉树的深度的延伸，有一个小技巧：不平衡就置为 1 ，之后就不用判断了。

```Python
class Solution(object):
    def isBalanced(self, root):

        def check(root):
            if not root: return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1
```

[返回目录](#205)

---

### 二叉树的最大路径和
#### 题目描述
给定一个非空的二叉树，找到最大路径总和。 对于此问题，路径定义为沿着父子连接从某个起始节点到树中任何节点的任何节点序列。 该路径必须至少包含一个节点，并且不需要经过根节点。
#### Python Solution：
**分析：** 比较经典的一道二叉树的题目，其实也是自底而上的递归调用，判断即可，同样有 trick 。

```Python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')

        def dfs(root):
            if not root:
                return 0
            left = max(0, dfs(root.left))   # left 和 right 与 0 取最大值方便了下面就不用判断了。
            right = max(0, dfs(root.right))
            val = root.val + left + right
            self.res = max(self.res, val)
            return root.val + max(left, right)

        dfs(root)
        return self.res
```

[返回目录](#206)

---

### 二叉树的最低公共祖先
#### 题目描述
给定二叉树，找到树中两个给定节点的最低公共祖先（LCA）。
#### Python Solution：
**分析：** 二叉树的题目考验递归比较多，这道题也是，迭代法想法还可以但是代码实现比较麻烦，不推荐。

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if root == p or root == q:
            return root
        m = self.lowestCommonAncestor(root.left,p,q)
        n = self.lowestCommonAncestor(root.right,p,q)
        if(m and n):
            return root
        elif m:
            return m
        else:
            return n
```

**可简化为**

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right
```
[返回目录](#207)

---

### 独特的路径
#### 题目描述
给定一个 m * n 的矩阵，求从左上角走到右下角有多少种走法。
#### Python Solution：
**分析：** 简单的动态规划，可以简化为一维 dp 。

```Python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] = dp[i-1] + dp[i]
        return dp[-1]
```

[返回目录](#301)

---

### House robber
#### 题目描述
给一组无序数组，求最大的子序列的和，但是相邻的数不能再一个序列里。
#### Python Solution：
**分析：** 其实就是 house robber 问题。简单题，可以从一维简化成常数量的空间复杂度。

```Python
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = cur = 0   # 为什么为零就可以了而不是 float('-inf')，因为负数就不考虑了。
        for i in range(len(nums)):
            cur, prev = max(prev + nums[i], cur), cur
        return cur
```

[返回目录](#302)

---

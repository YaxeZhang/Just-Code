<span id = "00"></span>
基础
 - [144. Binary Tree Preorder Traversal](#144-binary-tree-preorder-traversal)
 - [94. Binary Tree Inorder Traversal](#94-binary-tree-inorder-traversal)
 - [145. Binary Tree Postorder Traversal](#145-binary-tree-postorder-traversal)
 - [102. Binary Tree Level Order Traversal](#102-binary-tree-level-order-traversal)
 - [107. Binary Tree Level Order Traversal II](#107-binary-tree-level-order-traversal-ii)
 - [103. Binary Tree Zigzag Level Order Traversal](#103-binary-tree-zigzag-level-order-traversal)
 - [100. Same Tree](#100-same-tree)
 - [101. Symmetric Tree](#101-symmetric-tree)
 - [226. Invert Binary Tree](#226-invert-binary-tree)
 - [257. Binary Tree Paths](#257-binary-tree-paths)
 - [112. Path Sum](#112-path-sum)
 - [113. Path Sum II](#113-path-sum-ii)
 - [129. Sum Root to Leaf Numbers](#129-sum-root-to-leaf-numbers)
 - [298	Binary Tree Longest Consecutive Sequence] **?**
 - [111. Minimum Depth of Binary Tree](#111-minimum-depth-of-binary-tree)
 - [104. Maximum Depth of Binary Tree](#104-maximum-depth-of-binary-tree)
 - [662. Maximum Width of Binary Tree](#662-maximum-width-of-binary-tree)
 - [559. Maximum Depth of N-ary Tree](#559-maximum-depth-of-n-ary-tree)
 - [110. Balanced Binary Tree](#110-balanced-binary-tree)
 - [124. Binary Tree Maximum Path Sum](#124-binary-tree-maximum-path-sum)
 - [250	Count Univalue Subtrees] **?**
 - [366	Find Leaves of Binary Tree] **?**
 - [337	House Robber III]
 - [617. Merge Two Binary Trees](#617-merge-two-binary-trees)
 - [199. Binary Tree Right Side View](#199-binary-tree-right-side-view)
BST
 - [98. Validate Binary Search Tree](#98-validate-binary-search-tree)
 - [235. Lowest Common Ancestor of a Binary Search Tree](#235-lowest-common-ancestor-of-a-binary-search-tree)
 - [236. Lowest Common Ancestor of a Binary Tree](#236-lowest-common-ancestor-of-a-binary-tree)
 - [1123. Lowest Common Ancestor of Deepest Leaves](#1123-lowest-common-ancestor-of-deepest-leaves)
 - [108. Convert Sorted Array to Binary Search Tree](#108-convert-sorted-array-to-binary-search-tree)
 - [109. Convert Sorted List to Binary Search Tree](#109-convert-sorted-list-to-binary-search-tree)
 - [173. Binary Search Tree Iterator](#173-binary-search-tree-iterator)
 - [230. Kth Smallest Element in a BST](#230-kth-smallest-element-in-a-bst)
 - [297. Serialize and Deserialize Binary Tree](#297-serialize-and-deserialize-binary-tree)
 - [285	Inorder Successor in BST] **?**
 - [270	Closest Binary Search Tree Value] **?**
 - [272	Closest Binary Search Tree Value II] **?**
 - [99. Recover Binary Search Tree](#99-recover-binary-search-tree)
重要程度
 - [156	Binary Tree Upside Down] **?**
 - [114	Flatten Binary Tree to Linked List]
 - [255	Verify Preorder Sequence in Binary Search Tree] **?**
 - [333	Largest BST Subtree] **?**
 - [222. Count Complete Tree Nodes](#222-count-complete-tree-nodes)
 - [105. Construct Binary Tree from Preorder and Inorder Traversal](#105-construct-binary-tree-from-preorder-and-inorder-traversal)
 - [106. Construct Binary Tree from Inorder and Postorder Traversal](#106-construct-binary-tree-from-inorder-and-postorder-traversal)
 - [116. Populating Next Right Pointers in Each Node](#116-populating-next-right-pointers-in-each-node)
 - [117. Populating Next Right Pointers in Each Node II](#117-populating-next-right-pointers-in-each-node-ii)
 - [314	Binary Tree Vertical Order Traversal] **?**
 - [96. Unique Binary Search Trees](#96-unique-binary-search-trees)
 - [95. Unique Binary Search Trees II](#95-unique-binary-search-trees-ii)
 - [331. Verify Preorder Serialization of a Binary Tree](#331-verify-preorder-serialization-of-a-binary-tree)
 - [968. Binary Tree Cameras](#968-binary-tree-cameras)

## 144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

给定一个二叉树，返回其节点值的前序遍历。

**Example**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self,root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)

# More easier
class Solution:
    def preorderTraversal(self, root):
        return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```

**迭代法**

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
```

[返回目录](#00)

## 94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

给定一个二叉树，返回其节点值的中序遍历。

**Example**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self,root, res):
        if root:
            self.dfs(root.left, res)
            res.append(root.val)
            self.dfs(root.right, res)

# More easier
class Solution:
    def inorderTraversal(self, root):
        return [] if not root else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
```

**迭代法**

```python
class Solution:
    def inorderTraversal(self, root):
        res, stack = [], []
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

[返回目录](#00)

## 145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

给定一个二叉树，返回其节点值的后序遍历。

**Example**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self,root, res):
        if root:
            self.dfs(root.left, res)
            self.dfs(root.right, res)
            res.append(root.val)

# More easier
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []
```

**迭代法**

```python
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

[返回目录](#00)

## 102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

给定一个二叉树，返回其节点值的层次遍历。 （即，从左到右，逐级）。

**Example**

```
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
```

---

### Python Solution
**分析：** 分层存储，每次输出当层并且将下一层的在赋值到这里。

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root:
            level = [root]
            while level:
                res.append([node.val for node in level])
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res
```

[返回目录](#00)

## 107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

给定一个二叉树，返回其节点值的自下而上的级别顺序遍历。 （即，从左到右，从叶到根逐级）。

**Example**

```
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
```

---

### Python Solution
**分析：** 分层存储，每次输出当层并且将下一层的在赋值到这里。

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root:
            level = [root]
            while level:
                res.append([node.val for node in level])
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res[::-1]
```

[返回目录](#00)

## 103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

给定一个二叉树，返回其节点值的之字形级别顺序遍历。 （即，从左到右，然后从右到左进入下一个级别，并在它们之间交替）。

**Example**

```
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
```

---

### Python Solution
**分析：** 分层存储，每次输出当层并且将下一层的在赋值到这里。

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root:
            level = [root]
            flag = 1
            while level:
                res.append([node.val for node in level][::flag])
                level = [kid for node in level for kid in (node.left, node.right) if kid]
                flag *= -1
        return res
```

[返回目录](#00)

## 100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

给定两个二进制树，编写一个函数来检查它们是否相同。

如果两个二叉树在结构上相同并且节点具有相同的值，则认为它们是相同的。

**Example**

```
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```

---

### Python Solution
**分析：** 递归和迭代法。推荐递归。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
```

**DFS**

```Python
class Solution:
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if n1 and n2 and n1.val == n2.val:
                stack.append((n1.right, n2.right))
                stack.append((n1.left, n2.left))
            elif n1 is n2:
                continue
            else:
                return False
        return True
```

**BFS**

```Python
class Solution:
    def isSameTree(self, p, q):
        dq = collections.deque([(p, q)])
        while dq:
            n1, n2 = dq.popleft()
            if n1 and n2 and n1.val == n2.val:
                dq.extend([(n1.left, n2.left), (n1.right, n2.right)])
            elif n1 is n2:
                continue
            else:
                return False
        return True
```

[返回目录](#00)

## 101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

给定一棵二叉树，检查它是否是其自身的镜像（即，围绕其中心对称）。

**Example**

```
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, p, q):
        if p and q:
            return p.val == q.val and self.compare(p.left, q.right) and self.compare(p.right, q.left)
        return p is q
```

**迭代法**

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        dq = collections.deque([(root.left, root.right)])
        while dq:
            l, r = dq.popleft()
            if l and r and l.val == r.val:
                dq.extend([(l.right, r.left), (l.left, r.right)])
            elif l is r:
                continue
            else:
                return False
        return True
```

[返回目录](#00)

## 226. Invert Binary Tree

Invert a binary tree.

左右翻转二叉树。

**Example**

```
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

[返回目录](#00)

## 257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

给定一棵二叉树，返回所有从根到叶的路径。

**Example**

```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]
```

**迭代法**

```python
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths, stack = [], [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return paths
```

[返回目录](#00)

## 112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

给定一个二叉树和一个和，确定该树是否具有从根到叶的路径，以使该路径上的所有值加起来等于给定的和。

**Example**

```
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
```

**迭代法**

```python
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, cur = stack.pop()
            if not node.left and not node.right and cur == sum:
                return True
            if node.left:
                stack.append((node.left, cur + node.left.val))
            if node.right:
                stack.append((node.right, cur + node.right.val))
        return False
```

[返回目录](#00)

## 113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

给定一棵二叉树和一个和，找到所有从根到叶的路径，其中每个路径的和等于给定的和。

**Example**

```
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
```

---

### Python Solution
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

## 129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

给定一个仅包含0-9数字的二叉树，每个从根到叶的路径都可以表示一个数字。

一个示例是从根到叶的路径1-> 2-> 3，它表示数字123。

找到所有从根到叶的数字的总和。

**Example**

```
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def f(root):
            if not root:
                return []
            return [str(root.val) + path
                    for kid in (root.left, root.right) if kid
                    for path in f(kid)] or [str(root.val)]
        return sum(map(int,f(root)))
```

**迭代法**

```python
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, res = [(root, str(root.val))], 0
        while stack:
            node, st = stack.pop()
            if not node.left and not node.right:
                res += int(st)
            if node.left:
                stack.append((node.left, st + str(node.left.val)))
            if node.right:
                stack.append((node.right, st + str(node.right.val)))
        return res
```

[返回目录](#00)

## 111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

给定二叉树，找到其最小深度。 最小深度是沿着从根节点到最近的叶节点的最短路径的节点数。

**Example**

```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        if not root: return 0
        d = list(map(self.minDepth, (root.left, root.right)))
        return 1 + (min(d) or max(d))

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
```

**迭代法**

```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, res = [(root, 1)], float('inf')
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                res = min(res, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return res
```

[返回目录](#00)

## 104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

给定二叉树，找到其最大深度。

最大深度是沿着从根节点到最远叶节点的最长路径的节点数。

注意：叶子是没有子节点的节点。

**Example**

```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
```

---

### Python Solution
**分析：** 递归和迭代法。推荐递归。

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
```

**DFS**

```Python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return 0
        DFS = [] # stack
        DFS.append((root,1))
        while DFS:
            root, depth = DFS.pop()
            if depth > ans:
                ans = depth
            if root.left:
                DFS.append((root.left, depth + 1))
            if root.right:
                DFS.append((root.right, depth + 1))
        return ans
```

**BFS**

```Python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        dq = collections.deque([root])
        depth = 0
        while dq:
            len_dq = len(dq)
            for _ in range(len_dq):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            depth += 1
        return depth
```

[返回目录](#00)

## 662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

给定一棵二叉树，编写一个函数以获取给定树的最大宽度。 树的宽度是所有级别之间的最大宽度。 二进制树与完整的二进制树具有相同的结构，但是某些节点为空。 一层的宽度定义为末端节点之间的长度（该层中最左边和最右边的非空节点，其中末端节点之间的空节点也计入长度计算中。

**Example**

```
Example 1:

Input:

           1
         /   \
        3     2
       / \     \  
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input:

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input:

          1
         / \
        3   2
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input:

          1
         / \
        3   2
       /     \  
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

```
---

### Python Solution
**分析：** 其实是一道非常简单的题，不过要注意的是 pos 的值的递进。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        stack, res = [(root, 0, 0)], []
        while stack:
            node, depth, pos = stack.pop()
            if len(res) < depth + 1:
                res.append([])
            res[depth].append(pos)
            if node.left:
                stack.append((node.left, depth + 1, pos * 2))
            if node.right:
                stack.append((node.right, depth + 1, pos * 2 + 1))
        return max([max(res[i]) - min(res[i]) for i in range(len(res))]) + 1
```

[返回目录](#00)

## 559. Maximum Depth of N-ary Tree

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

给定n元树，找到其最大深度。 最大深度是沿着从根节点到最远叶节点的最长路径的节点数。


---

### Python Solution
**分析：** 其实和二叉树的最大深度类似，只是多加了个循环。

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(node) for node in root.children) + 1  
```

[返回目录](#00)

## 110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

给定一棵二叉树，确定它是否是高度平衡的。

对于此问题，将高度平衡的二叉树定义为： 一棵二叉树，其中每个节点的两个子树的深度相差不超过1。

**Example**

```
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
```

---

### Python Solution
**分析：**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

[返回目录](#00)

## 124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

给定一个非空的二叉树，找到最大路径总和。 对于此问题，路径定义为沿着父子连接从某个起始节点到树中任何节点的任何节点序列。 该路径必须至少包含一个节点，并且不需要经过根节点。

**Example**

```
Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

---

### Python Solution
**分析：**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        def dfs(root):
            if not root: return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            val = root.val + left + right
            self.res = max(self.res, val)
            return root.val + max(left, right)
        dfs(root)
        return self.res
```

[返回目录](#00)

## 617. Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

给定两棵二叉树，想象一下，当您将其中一棵树覆盖另一棵树时，两棵树的某些节点是重叠的，而其他树则没有。

您需要将它们合并到新的二叉树中。 合并规则是，如果两个节点重叠，则将节点值加起来作为合并节点的新值。 否则，非空节点将用作新树的节点。

---

### Python Solution
**分析：** 递归的做法比较简单，迭代的做法待补充。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        else:
            return t1 or t2
```

[返回目录](#00)

## 199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

给定一个二叉树，想象一下自己站在树的右侧，返回从上到下可以看到的节点的值。

**Example**

```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

---

### Python Solution
**分析：** 考察的是 BST 。

**BST**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            level = [root]
            while level:
                res.append(level[-1].val)
                level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return res
```

[返回目录](#00)

## 98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

给定一个二叉树，请确定它是否为有效的二叉树（BST）。

假设BST定义如下：

节点的左子树仅包含键小于节点键的节点。
节点的右子树仅包含键大于该节点的键的节点。
左子树和右子树都必须也是二进制搜索树。

**Example**

```
  5
 / \
1   4
   / \
  3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

---

### Python Solution
**分析：**

**递归大法好啊，简单又方便**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isValidBST(self, root: TreeNode, lower=float('-inf'), upper=float('inf')) -> bool:
        return not root or (lower < root.val < upper
		       and (self.isValidBST(root.left, lower, root.val) if root.left else True)
			   and (self.isValidBST(root.right, root.val, upper) if root.right else True))

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(root, big, small):
            if not root: return True
            if root.val >= big or root.val <= small: return False
            return validate(root.left, root.val, small) and validate(root.right, big, root.val)
        return validate(root, float('inf'), float('-inf'))
```

**利用 BST 中序遍历的性质**

```python
class Solution:      # 效率居高，推荐这一种解法
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        cur = root
        pre = None
        while len(stack) or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                p = stack.pop()
                if pre and p.val <= pre.val:
                    return False
                pre = p
                cur = p.right
        return True

class Solution:       # 效率极低
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            return [] if not root else inorder(root.left) + [root.val] + inorder(root.right)
        tmp = inorder(root)
        for i in range(1, len(tmp)):
            if tmp[i] <= tmp[i - 1]:
                return False
        return True

class Solution:      # 效率还可以
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
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
        tmp = inorder(root)
        for i in range(1, len(tmp)):
            if tmp[i] <= tmp[i - 1]:
                return False
        return True
```

[返回目录](#00)

## 235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

给定二叉搜索树（BST），请在BST中找到两个给定节点的最低公共祖先（LCA）。

根据Wikipedia上LCA的定义：“最低的共同祖先被定义为两个节点p和q之间，这是T中同时具有p和q作为后代的最低节点（在这里我们允许节点成为其自身的后代）。 ”

**Example**

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
```

**迭代法**

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:     # root.val 在左右中间，那么 root 就是最低公共祖先
            root = (root.left, root.right)[p.val > root.val]
        return root
```

[返回目录](#00)

## 236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

给定二叉树，找到树中两个给定节点的最低公共祖先（LCA）。

根据Wikipedia上LCA的定义：“最低的共同祖先定义为两个节点p和q之间，作为T中同时具有p和q作为后代的最低节点（我们允许节点成为其自身的后代）。 ”

**Example**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

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

**迭代法**

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        stack = [root]
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]

        while q not in ancestors:
            q = parents[q]
        return q
```

[返回目录](#00)

## 1123. Lowest Common Ancestor of Deepest Leaves

Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.

给定一棵有根的二叉树，返回其最深叶的最低共同祖先。

回想一下：

二叉树的节点只有当没有子节点时才是叶子。树的根深度为0，并且如果节点的深度为d，则其每个子节点的深度为d +1。 一组节点S中最低的公共祖先是深度最大的节点A，这样S中的每个节点都在具有根A的子树中。

**Example**

```
Input: root = [1,2,3]
Output: [1,2,3]
Explanation:
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".
```

---

### Python Solution
**分析：** 分为两个解法，一种是递归的做法，另外一种是迭代的做法。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):

        def helper(root):
            if root is None:
                return [None,0]
            left = helper(root.left)
            right = helper(root.right)
            maxh = max(left[1],right[1])
            if left[1] < right[1]:
                return [right[0],maxh+1]
            elif left[1] > right[1]:
                return [left[0],maxh+1]
            else:
                return [root,maxh+1]
        res = helper(root)
        return res[0]
```

**迭代法**

```python

```

[返回目录](#00)

## 108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

给定一个数组，其中元素按升序排序，请将其转换为高度平衡的BST。 对于此问题，将高度平衡的二叉树定义为二叉树，其中每个节点的两个子树的深度相差不超过1。

**Example**

```
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

---

### Python Solution
**分析：** 很简单弱智的题目。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
```

[返回目录](#00)

## 109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

给定一个单链列表，其中元素按升序排序，请将其转换为高度平衡的BST。 对于此问题，将高度平衡的二叉树定义为二叉树，其中每个节点的两个子树的深度相差不超过1。

**Example**

```
Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

---

### Python Solution
**分析：** 递归的做法，也可以用额外空间的迭代，但是没有意义。细节是把链表分为两端。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return
        if not head.next: return TreeNode(head.val)
        slow, fast, pre = head, head, None
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None   # cut off the left half

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
```

[返回目录](#00)

## 173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

在二叉搜索树（BST）上实现迭代器。您的迭代器将使用BST的根节点进行初始化。 调用next（）将返回BST中的下一个最小数字

**Example**

```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
```

---

### Python Solution
**分析：** 考察的是二叉搜索树的中序遍历。

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        self.visit = root
        self.stack = []

    def next(self):
        while self.visit:
            self.stack.append(self.visit)
            self.visit = self.visit.left
        node = self.stack.pop()
        self.visit = node.right
        return node.val

    def hasNext(self):
        return self.visit or self.stack



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

[返回目录](#00)

## 230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

给定一个二叉搜索树，编写一个函数kthSmallest在其中找到第k个最小的元素。

**Example**

```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1


Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

---

### Python Solution
**分析：**


**迭代法**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack= []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            k -= 1
            if not k: return node.val
            root = node.right
        return None
```

[返回目录](#00)

## 297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

序列化是将数据结构或对象转换为位序列的过程，以便可以将其存储在文件或内存缓冲区中，或者通过网络连接链接进行传输，以便稍后在相同或另一个计算机环境中进行重构。 设计一种用于对二叉树进行序列化和反序列化的算法。 序列化/反序列化算法的工作方式没有任何限制。 您只需要确保可以将二叉树序列化为字符串，并且可以将该字符串反序列化为原始树结构。

**Example**

```
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
```

---

### Python Solution
**分析：**  考察的其实就是遍历和恢复，不过突出点在 iter() 和 next() 上。


**迭代法**

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

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

## 99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

二叉搜索树（BST）的两个元素被错误交换。 恢复树而不更改其结构。

**Example**

```
Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
```

---

### Python Solution
**分析：**  中序遍历然后找出出问题的两个结点，交换值即可。


**迭代法**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        cur = root
        stack, res = [], []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node)
            cur = node.right
        first, second = None, None
        for i in range(1, len(res)):
            if not first and res[i-1].val > res[i].val:
                first, second = res[i-1], res[i]
            if first and res[i-1].val > res[i].val:
                second = res[i]
        first.val, second.val = second.val, first.val
```

```python
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        pre = first = second = None
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val > root.val:
                second = root
                if not first:
                    first = pre
                else:
                    break
            pre = root
            root = root.right

        if first and second:
            first.val, second.val = second.val, first.val
```

[返回目录](#00)

## 222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

给定完整的二叉树，计算节点数。

**Example**

```
Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
```

---

### Python Solution
**分析：** 考验的思想应该是二分法，要充分利用完全二叉树的性质。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
```

[返回目录](#00)

## 105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

给定一棵树的前序和有序遍历，构造二叉树。

注意： 您可以假定树中不存在重复项。

**Example**

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
```

---

### Python Solution
**分析：** 和下面一题的思路一样，复杂写法不再赘述，看下一题的分析即可。

```python
class Solution:
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

[返回目录](#00)

## 106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

给定一棵树的有序和后序遍历，构造二叉树。

注意： 您可以假定树中不存在重复项。

**Example**

```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
```

---

### Python Solution
**分析：** 两种都非常好理解，第一种是找到根节点，然后将 inorder 查分为两半继续寻找，问题在于如何找到 根节点在 inorder 的位置，下面第一种解法有点傻，更高效的是建立一个哈希表，占用 O(n) 的空间、查询时间为O(1)。第二种解法呢则非常聪明，不用找根节点的位置，构建 root.right 时每次都调用的是 postorder 最后一个元素，终点是 root.val 。构建 root.right 的时候终点是 None。

```python
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root
```

**easier**

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def postdfs(stop):
            if postorder and inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = postdfs(root.val)
                inorder.pop()
                root.left = postdfs(stop)
                return root
        return postdfs(None)
```

[返回目录](#00)

## 116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

您将得到一棵完美的二叉树，其中所有叶子都在同一水平上，每个父级都有两个孩子。

填充每个下一个指针以指向其下一个右节点。 如果没有下一个右节点，则下一个指针应设置为NULL。

最初，所有下一个指针都设置为NULL。

---

### Python Solution
**分析：** 递归法，需要额外空间的迭代法，不需要额外空间的迭代法。思路简单易懂。

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def ans(root):
            if not root:
                return
            if not root.left or not root.right:
                return
            root.left.next = root.right
            if root.next and root.next.left:
                root.right.next = root.next.left
            ans(root.left)
            ans(root.right)
            return

        ans(root)
        return root
```

**额外空间的迭代法**

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        cur = [root]
        while cur:
            for i in range(len(cur) - 1):
                cur[i].next = cur[i+1]
            cur = [node for n in cur for node in (n.left, n.right) if node]
        return root
```

**O(1)空间的迭代法**

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        cur, tmp = root, root.left
        while cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = tmp
                tmp = cur.left
        return root
```

[返回目录](#00)

## 117. Populating Next Right Pointers in Each Node II

Similar to the previous question, but the complete binary tree is changed to an ordinary binary tree.

和上一题大致类似，不过完全二叉树改为一颗普通的二叉树。

---

### Python Solution
**分析：** 需要额外空间的迭代法，不需要额外空间的迭代法。思路简单易懂。

**额外空间的迭代法**

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        cur = [root]
        while cur:
            for i in range(len(cur) - 1):
                cur[i].next = cur[i+1]
            cur = [node for n in cur for node in (n.left, n.right) if node]
        return root
```

[返回目录](#00)

## 96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

给定n，多少个结构唯一的BST（二进制搜索树）存储值1 ... n？

**Example**

```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

---

### Python Solution
**分析：** Catalan number

```python
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0 for i in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i//2):
                dp[i] += dp[j] * dp[i - 1 - j] * 2        
            if i % 2 != 0:
                dp[i] += dp[i//2] * dp[i//2]        
        return dp[-1]
```

**数学解法**

```python
class Solution:
    def numTrees(self, n: int) -> int:
        ans = 1
        for i in range(1, n+1):
            ans = ans*(i+n)/i
        return int(ans/(n+1))
```

[返回目录](#00)

## 95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

给定整数n，生成所有存储值1 ... n的结构上唯一的BST（二进制搜索树）。

**Example**

```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

---

### Python Solution
**分析：** Catalan number

```python
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        memo = {}

        def subtrees(start, end):
            if start > end: return [None]
            if (start, end) in memo: return memo[(start, end)]
            ans = []
            for i in range(start, end+1):
                left = subtrees(start, i-1)
                right = subtrees(i+1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            memo[(start, end)] = ans
            return ans

        return subtrees(1, n) if n >= 1 else []
```

**简单但慢**

```python
from functools import lru_cache
class Solution:
    def generateTrees(self, n):
        if not n: return []
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        @lru_cache(maxsize=None)
        def trees(first, last):
            return [node(root, left, right)
                    for root in range(first, last+1)
                    for left in trees(first, root-1)
                    for right in trees(root+1, last)] or [None]
        return trees(1, n)
```

[返回目录](#00)

## 331. Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

序列化二叉树的一种方法是使用顺序遍历。当我们遇到非空节点时，我们记录该节点的值。如果它是一个空节点，我们将使用诸如＃之类的前哨值进行记录。

**Example**

```
Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false
```

---

### Python Solution
**分析：** 利用了二叉树的一个性质，空结点的个数比非空结点的个数多一个。

```python
class Solution(object):
    def isValidSerialization(self, preorder):
        s = 1
        for is_null in map(lambda c: c == '#', preorder.split(',')):
            if not s:
                return False     
            s = s - 1 if is_null else s + 1              
        return not s
```

[返回目录](#00)

## 968. Binary Tree Cameras

Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

给定一棵二叉树，我们在树的节点上安装摄像机。 节点上的每个摄像机都可以监视其父代，自身及其直系子代。 计算监视树的所有节点所需的最少摄像机数量。

**Example**

```
Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
```

---

### Python Solution
**分析：** 这是一道 hard 的题，但是理解了之后会觉得思路很清晰、简单。一种方法是利用递归到达最底端，标记 3 种状态，0 是未监管，1 是当前结点有摄像机，2 是为空或者被子代的摄像机监管。这样就非常好处理，自底向上推导并记录摄像机的个数。另一种是动态规划，可以理解一下。两种方法对于状态的定义码不一样，看的时候不要混淆。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 2
            l = dfs(node.left)
            r = dfs(node.right)
            if l==0 or r ==0:
                self.res += 1
                return 1
            if l == 1 or r == 1 :
                return 2
            return 0

        return (dfs(root) == 0) + self.res
```

```python
class Solution(object):
    def minCameraCover(self, root):
        def solve(node):
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node: return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(solve(root)[1:])
```

[返回目录](#00)

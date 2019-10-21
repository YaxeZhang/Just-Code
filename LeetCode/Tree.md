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
 - [298	Binary Tree Longest Consecutive Sequence]
 - [111. Minimum Depth of Binary Tree](#111-minimum-depth-of-binary-tree)
 - [104. Maximum Depth of Binary Tree](#104-maximum-depth-of-binary-tree)
 - [559. Maximum Depth of N-ary Tree](#559-maximum-depth-of-n-ary-tree)
 - [110. Balanced Binary Tree](#110-balanced-binary-tree)
 - [124	Binary Tree Maximum Path Sum]
 - [250	Count Univalue Subtrees]
 - [366	Find Leaves of Binary Tree]
 - [337	House Robber III]
 - [617. Merge Two Binary Trees](#617-merge-two-binary-trees)
 - [199. Binary Tree Right Side View](#199-binary-tree-right-side-view)
BST
 - [98. Validate Binary Search Tree](#98-validate-binary-search-tree)
 - [235. Lowest Common Ancestor of a Binary Search Tree](#235-lowest-common-ancestor-of-a-binary-search-tree)
 - [236. Lowest Common Ancestor of a Binary Tree](#236-lowest-common-ancestor-of-a-binary-tree)
 - [1123. Lowest Common Ancestor of Deepest Leaves](#1123-lowest-common-ancestor-of-deepest-leaves)
 - [108	Convert Sorted Array to Binary Search Tree]
 - [109	Convert Sorted List to Binary Search Tree]
 - [173	Binary Search Tree Iterator]
 - [230. Kth Smallest Element in a BST](#230-kth-smallest-element-in-a-bst)
 - [297	Serialize and Deserialize Binary Tree]
 - [285	Inorder Successor in BST]
 - [270	Closest Binary Search Tree Value]
 - [272	Closest Binary Search Tree Value II]
 - [99	Recover Binary Search Tree]
重要程度
 - [156	Binary Tree Upside Down]
 - [114	Flatten Binary Tree to Linked List]
 - [255	Verify Preorder Sequence in Binary Search Tree]
 - [333	Largest BST Subtree]
 - [222	Count Complete Tree Nodes]
 - [105. Construct Binary Tree from Preorder and Inorder Traversal](#105-construct-binary-tree-from-preorder-and-inorder-traversal)
 - [106. Construct Binary Tree from Inorder and Postorder Traversal](#106-construct-binary-tree-from-inorder-and-postorder-traversal)
 - [116	Populating Next Right Pointers in Each Node]
 - [117	Populating Next Right Pointers in Each Node II]
 - [314	Binary Tree Vertical Order Traversal]
 - [96	Unique Binary Search Trees]
 - [95	Unique Binary Search Trees II]
 - [331	Verify Preorder Serialization of a Binary Tree]

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

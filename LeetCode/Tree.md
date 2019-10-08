<span id = "00"></span>
基础
 - [144. Binary Tree Preorder Traversal](#144-binary-tree-preorder-traversal)
 - [94. Binary Tree Inorder Traversal](#94-binary-tree-inorder-traversal)
 - [145. Binary Tree Postorder Traversal](#145-binary-tree-postorder-traversal)
 - [102. Binary Tree Level Order Traversal](#102-binary-tree-level-order-traversal)
 - [107. Binary Tree Level Order Traversal II](#107-binary-tree-level-order-traversal-ii)
 - [100	Same Tree]
 - [101	Symmetric Tree]
 - [226	Invert Binary Tree]
 - [257	Binary Tree Paths]
 - [112	Path Sum]
 - [113	Path Sum II]
 - [129	Sum Root to Leaf Numbers]
 - [298	Binary Tree Longest Consecutive Sequence]
 - [111	Minimum Depth of Binary Tree]
 - [104. Maximum Depth of Binary Tree](#104-maximum-depth-of-binary-tree)
 - [559. Maximum Depth of N-ary Tree](#559-maximum-depth-of-n-ary-tree)
 - [110	Balanced Binary Tree]
 - [124	Binary Tree Maximum Path Sum]
 - [250	Count Univalue Subtrees]
 - [366	Find Leaves of Binary Tree]
 - [337	House Robber III]
 - [617. Merge Two Binary Trees](#617-merge-two-binary-trees)
BFS
 - [103	Binary Tree Zigzag Level Order Traversal]
 - [199	Binary Tree Right Side View]class Solution:
BST
 - [98	Validate Binary Search Tree]
 - [235	Lowest Common Ancestor of a Binary Search Tree]
 - [236	Lowest Common Ancestor of a Binary Tree]
 - [108	Convert Sorted Array to Binary Search Tree]
 - [109	Convert Sorted List to Binary Search Tree]
 - [173	Binary Search Tree Iterator]
 - [230	Kth Smallest Element in a BST]
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
 - [105	Construct Binary Tree from Preorder and Inorder Traversal]
 - [106	Construct Binary Tree from Inorder and Postorder Traversal]
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
        if not root:
            return []
        level, res = [root], []
        while level:
            res.append([node.val for node in level])
            tmp = [(node.left, node.right) for node in level]
            level = [leaf for n in tmp for leaf in n if leaf]
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level, res = [root], []
        while level:
            res.append([node.val for node in level])
            tmp = [(node.left, node.right) for node in level]
            level = [leaf for n in tmp for leaf in n if leaf]
        return res[::-1]
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

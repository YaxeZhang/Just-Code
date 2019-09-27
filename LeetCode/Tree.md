<span id = "00"></span>
基础
 - [144. Binary Tree Preorder Traversal](#144-binary-tree-preorder-traversal)
 - [94. Binary Tree Inorder Traversal](#94-binary-tree-inorder-traversal)
 - [145	Binary Tree Postorder Traversal]
 - [102	Binary Tree Level Order Traversal]
Preorder
 - [100	Same Tree]
 - [101	Symmetric Tree]
 - [226	Invert Binary Tree]
 - [257	Binary Tree Paths]
 - [112	Path Sum]
 - [113	Path Sum II]
 - [129	Sum Root to Leaf Numbers]
 - [298	Binary Tree Longest Consecutive Sequence]
 - [111	Minimum Depth of Binary Tree]
Preorder
 - [104	Maximum Depth of Binary Tree]
 - [110	Balanced Binary Tree]
 - [124	Binary Tree Maximum Path Sum]
 - [250	Count Univalue Subtrees]
 - [366	Find Leaves of Binary Tree]
 - [337	House Robber III]
BFS
 - [107	Binary Tree Level Order Traversal II]
 - [103	Binary Tree Zigzag Level Order Traversal]
 - [199	Binary Tree Right Side View]
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

# 更剪短些
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

# 更剪短些
class Solution:
    def inorderTraversal(self, root):
        return [] if not root else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
```

**迭代法**

```python
class Solution:
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
```

[返回目录](#00)

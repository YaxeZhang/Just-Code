# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        if not root:
            return
        root.val = 0
        self.recover(root)
        return
    def recover(self, root):
        if not root:
            return
        if root.left:
            root.left.val = root.val * 2 + 1
            self.recover(root.left)
        if root.right:
            root.right.val = root.val * 2 + 2
            self.recover(root.right)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        node = self.root
        encoding = bin(target + 1)[3:]
        counter = 0
        while counter < len(encoding):
            if encoding[counter] == "0":
                if node.left:
                    node = node.left
                    counter += 1
                else:
                    return False
            else:
                if node.right:
                    node = node.right
                    counter += 1
                else:
                    return False
        return True
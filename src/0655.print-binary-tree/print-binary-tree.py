# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def get_height(node):
            return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))
        
        def update_output(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            self.output[row][mid] = str(node.val)
            update_output(node.left, row + 1 , left, mid - 1)
            update_output(node.right, row + 1 , mid + 1, right)
            
        height = get_height(root)
        width = 2 ** height - 1
        self.output = [[''] * width for i in range(height)]
        update_output(node=root, row=0, left=0, right=width - 1)
        return self.output
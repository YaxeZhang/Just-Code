# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def increasingBST(self, root):
		def in_order(node):
			if not node:
				return []
			return in_order(node.left) + [node] + in_order(node.right)


		# get list of nodes in order
		nodelist = in_order(root)

		# update node pointers
		for i in range(len(nodelist)-1):
			nodelist[i].left = None
			nodelist[i].right = nodelist[i+1]

		nodelist[-1].left = None
		nodelist[-1].right = None

		return nodelist[0]
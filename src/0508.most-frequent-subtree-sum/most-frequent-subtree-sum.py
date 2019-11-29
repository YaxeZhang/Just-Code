# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            vals.append(left + right + root.val)
            return left + right + root.val
        
        vals = []
        dfs(root)
        count = collections.Counter(vals)
        maxcnt = max(count.values())
        return [x for x in count if count[x] == maxcnt]
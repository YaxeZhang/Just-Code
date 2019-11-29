# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0
        cache = collections.defaultdict(int)
        cache[0] = 1
        
        def dfs(root, cur_sum):
            if not root:
                return 
            cur_sum += root.val
            self.ans += cache[cur_sum - sum]
            cache[cur_sum] += 1
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            cache[cur_sum] -= 1
            
        dfs(root, 0)
        return self.ans
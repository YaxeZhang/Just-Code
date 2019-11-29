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
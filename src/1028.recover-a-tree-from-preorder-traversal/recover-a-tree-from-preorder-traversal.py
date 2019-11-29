class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S: return
        l = S.split('-')
        s, depth = [[TreeNode(l[0]), 0]], 1
        for item in l[1:]:
            if not item:
                depth += 1
                continue
            node = TreeNode(item)
            while s[-1][1] != depth - 1:
                s.pop()
            if not s[-1][0].left: 
                s[-1][0].left = node
            else:
                s[-1][0].right = node
            s.append([node, depth])
            depth = 1
        return s[0][0]
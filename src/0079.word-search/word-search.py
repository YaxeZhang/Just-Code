class Solution:
    def exist(self, matrix: List[List[str]], string: str) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        state = [[True] * n for _ in range(m)]
        
        def dfs(i, j, pos):
            if 0 <= i < m and 0 <= j < n and state[i][j]:
                state[i][j] = ret = False
                if matrix[i][j] == string[pos]:
                    if pos == len(string) - 1:
                        return True
                    ret = dfs(i, j-1, pos+1) or dfs(i, j+1, pos+1) or dfs(i-1, j, pos+1) or dfs(i+1, j, pos+1)
                if not ret: 
                    state[i][j] = True
                return ret
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == string[0]:
                    if dfs(i, j, 0):
                        return True
        return False
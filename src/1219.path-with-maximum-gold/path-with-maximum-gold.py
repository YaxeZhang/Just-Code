class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in seen and grid[i][j] != 0:
                    val, path = self.DFS(grid, i, j)
                    if val > res:
                        res = val
                        seen = path
        return res
    
    def DFS(self, grid, i, j):
        v, path = 0, set() ## v: 从该节点往后最长路径的值(不包含该节点), path:从该节点往后最长路径(不包含该节点)
        tmp_val = grid[i][j]
        grid[i][j] = 0
        if i > 0 and grid[i-1][j] != 0:
            s, tmp = self.DFS(grid, i-1, j)
            if s > v:
                v = s
                path = tmp
        if i < len(grid) - 1 and grid[i+1][j] != 0:
            s, tmp = self.DFS(grid, i+1, j)
            if s > v:
                v = s
                path = tmp
        if j > 0 and grid[i][j-1] != 0:
            s, tmp = self.DFS(grid, i, j - 1)
            if s > v:
                v = s
                path = tmp
        if j < len(grid[0]) - 1 and grid[i][j + 1] != 0:
            s, tmp = self.DFS(grid, i, j+1)
            if s > v:
                v = s
                path = tmp
        
        grid[i][j] = tmp_val
                
        return v + tmp_val, path | {(i, j)}
        

        return max_v